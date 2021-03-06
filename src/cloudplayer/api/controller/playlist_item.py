"""
    cloudplayer.api.controller.playlist_item
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2018 by Nicolas Drebenstedt
    :license: GPL-3.0, see LICENSE for details
"""
from cloudplayer.api.access import Available
from cloudplayer.api.controller import Controller, ControllerException
from cloudplayer.api.controller.track import TrackController
from cloudplayer.api.model.playlist import Playlist
from cloudplayer.api.model.playlist_item import PlaylistItem


class PlaylistItemController(Controller):

    __model__ = PlaylistItem

    async def create(self, ids, kw, fields=Available):
        track_id = kw.get('track_id')
        track_provider_id = kw.get('track_provider_id')
        track_controller = TrackController.for_provider(
            track_provider_id, self.db, self.current_user)
        track = await track_controller.read({
            'id': track_id, 'provider_id': track_provider_id})
        if not track:
            raise ControllerException(404, 'track not found')

        playlist = self.db.query(Playlist).get(
            (ids.pop('playlist_id'), ids.pop('playlist_provider_id')))
        if not playlist:
            raise ControllerException(404, 'playlist not found')

        if not playlist.image:
            playlist.image = track.image.copy()
            self.db.add(playlist)

        return await super().create(ids, kw, fields=fields)

    async def query(self, ids, kw):
        query = await super().query(ids, kw)
        return query.order_by(PlaylistItem.rank)
