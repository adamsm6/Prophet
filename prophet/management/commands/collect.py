from django.core.management.base import BaseCommand
from prophet import historicalDataFetcher as fetcher
from prophet import coinTableObserver as coin_obs
from prophet import mlObserver as ml_obs


class Command(BaseCommand):
    help = 'Collects data'

    def add_argument(self, parser):
        pass

    # Create subject to fetch coin data and attach observers
    # to update database and ML predictions
    def handle(self, *args, **options):
        url = "https://api.coinmarketcap.com/v1/ticker/"
        historical_puller = fetcher.HistoricalDataFetcher(url)
        coin_obs.CoinTableObserver(historical_puller)
        ml_obs.MLObserver(historical_puller)
        historical_puller.collect_data()
