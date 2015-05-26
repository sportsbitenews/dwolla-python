'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  This file contains functionality for all accounts related endpoints.
'''

from . import constants as c
from .rest import r

def basic(aid, **kwargs):
    """
    Returns basic account info for the passed account ID.

    :param aid: String of account ID.
    :return: Dictionary with account information.
    """
    if not aid:
        raise Exception('basic() requires aid parameter')


    return r._get('/users/' + aid,
                     {
                         'client_id': kwargs.pop('client_id', c.client_id),
                         'client_secret': c.client_secret
                     }, dwollaparse=kwargs.pop('dwollaparse', 'dwolla'))

def full(**kwargs):
    """
    Returns full account information for the user associated
    with the currently set OAuth token.

    :return: Dictionary with account information.
    """
    return r._get('/users',
                     {
                         'oauth_token': kwargs.pop('alternate_token', c.access_token)
                     }, dwollaparse=kwargs.pop('dwollaparse', 'dwolla'))

def balance(**kwargs):
    """
    Gets balance for the account associated with the
    currently set OAuth token.

    :return: Balance
    """
    return r._get('/balance', 
                    {
                        'oauth_token': kwargs.pop('alternate_token', c.access_token)
                    }, dwollaparse=kwargs.pop('dwollaparse', 'dwolla'))

def nearby(lat, lon, **kwargs):
    """
    Returns users and venues near a location.

    :param lat: Double containing latitude.
    :param lon: Double containing longitude.
    :return: Dictionary with venues and users.
    """
    if not lat:
        raise Exception('nearby() requires lat parameter')
    if not lon:
        raise Exception('nearby() requires lon parameter')

    return r._get('/users/nearby',
                     {
                         'client_id': kwargs.pop('client_id', c.client_id),
                         'client_secret': c.client_secret,
                         'latitude': lat,
                         'longitude': lon
                     }, dwollaparse=kwargs.pop('dwollaparse', 'dwolla'))

def autowithdrawalstatus(**kwargs):
    """
    Gets auto withdrawal status for the account associated
    with the currently set OAuth token.
    :return: AW status for account.
    """
    return r._get('/accounts/features/auto_withdrawl',
                  {
                      'oauth_token': kwargs.pop('alternate_token', c.access_token)
                  }, dwollaparse=kwargs.pop('dwollaparse', 'dwolla'))

def toggleautowithdrawalstatus(status, fid, **kwargs):
    """
    Sets auto-withdrawal status of the account associated
    with the current OAuth token under the specified
    funding ID.
    :param status: Boolean for toggle.
    :param fid: String with funding ID for target account
    :return: String (Either "Enabled" or "Disabled")
    """
    if not status:
        raise Exception('toggleautowithdrawlstatus() requires status parameter')
    if not fid:
        raise Exception('toggleautowithdrawlstatus() requires fid parameter')

    return r._post('/accounts/features/auto_withdrawl',
                   {
                       'oauth_token': kwargs.pop('alternate_token', c.access_token),
                       'enabled': status,
                       'fundingId': fid
                   }, dwollaparse=kwargs.pop('dwollaparse', 'dwolla'))



