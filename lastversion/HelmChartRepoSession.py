from .ProjectHolder import ProjectHolder
import logging

log = logging.getLogger(__name__)
import yaml


class HelmChartRepoSession(ProjectHolder):

    def __init__(self, url):
        super(HelmChartRepoSession, self).__init__()
        self.url = url

    def get_latest(self, pre_ok=False, major=None):
        # https://github.com/bitnami/charts/blob/master/bitnami/aspnet-core/Chart.yaml
        # https://raw.githubusercontent.com/bitnami/charts/master/bitnami/aspnet-core/Chart.yaml
        url = self.url.replace('github.com', 'raw.githubusercontent.com').replace('/blob/', '/')
        r = self.get(url)
        chart_data = yaml.safe_load(r.text)
        return {
            'tag_name': None,
            'tag_date': None,
            'version': self.sanitize_version(chart_data['version'], pre_ok, major),
            'type': 'helm'
        }