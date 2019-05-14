#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for `coal_node` obsplus dataset.
"""
from pathlib import Path

import obsplus
import pytest
import obspy
from obsplus.interfaces import EventClient, WaveformClient, StationClient

CLIENT_TYPE = {
    "waveform": WaveformClient,
    "event": EventClient,
    "station": StationClient,
}


@pytest.fixture(scope="session")
def dataset():
    """
    Load the new dataset via obsplus plugin.
    """
    return obsplus.load_dataset("coal_node")


@pytest.fixture(scope="session")
def clients(dataset):
    """ return a dict of clients. """
    clients = dict(
        waveform=dataset.waveform_client,
        event=dataset.event_client,
        station=dataset.station_client,
    )
    return clients


def test_dataset(dataset):
    """ A simple tests to make sure the data have been loaded. """
    assert Path(dataset.path).exists()


def test_return_clients(clients):
    """ Ensure each client type is returned. """
    for cli_type, client in clients.items():
        expected_type = CLIENT_TYPE[cli_type]
        assert isinstance(client, expected_type) or client is None


def test_waveforms(clients):
    """ Clients should return waveforms """
    st = clients["waveform"].get_waveforms()
    assert isinstance(st, obspy.Stream)
    assert len(st)


def test_events(clients):
    """ Clients to return event data. """
    events = clients["event"].get_events()
    assert isinstance(events, obspy.Catalog)
    assert len(events)


def test_inventory(clients):
    """ CLient should return station data """
    station = clients["station"].get_stations()
    assert isinstance(station, obspy.Inventory)
    assert len(station)
