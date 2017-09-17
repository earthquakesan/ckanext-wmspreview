import logging
import urllib

import ckan.plugins as p

log = logging.getLogger(__name__)

try:
    import ckanext.resourceproxy.plugin as proxy
except ImportError:
    pass


class WMSPreview(p.SingletonPlugin):
    '''This extension previews WMS resources.'''
    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IConfigurable, inherit=True)
    p.implements(p.IResourcePreview, inherit=True)

    WMS = ['WMS', 'wms']
    arcgis_webmap_viewer_url = "http://www.arcgis.com/home/webmap/viewer.html"
    arcgis_webmap_viewer_url_embed = "//www.arcgis.com/apps/Embed/index.html"
    webmap_viewer_params = {
        "url": "http://wms.leipzig.de/arcgis/rest/services/wms/BRW/MapServer",
        "source": "sd",
        "mapOnly": "true"
    }
    webmap_viewer_embed_params = {
        "webmap": "0d1cdb69256e4f67b8be1887b7822d02",
        "extent": "12.143,51.2496,12.6329,51.4383",
        "home": "true",
        "zoom": "true",
        "previewImage": "false",
        "scale": "true",
        "search": "true",
        "searchextent": "true",
        "disable_scroll": "true",
        "theme": "light"

    }
    leipzig_wms_namespace = "wms.leipzig.de"

    def update_config(self, config):
        p.toolkit.add_public_directory(config, 'theme/public')
        p.toolkit.add_template_directory(config, 'theme/templates')
        p.toolkit.add_resource('theme/public', 'ckanext-wmspreview')

    def configure(self, config):
        enabled = config.get('ckan.resource_proxy_enabled', False)
        self.proxy_is_enabled = enabled

    def can_preview(self, data_dict):
        resource = data_dict['resource']
        format_lower = resource['format'].lower()
        if format_lower in self.WMS and \
                resource['url'].find(self.leipzig_wms_namespace) != -1:
            return {'can_preview': True, 'quality': 2}
        return {'can_preview': False}

    def setup_template_variables(self, context, data_dict):
        if (self.proxy_is_enabled
                and not data_dict['resource']['on_same_domain']):
            url = proxy.get_proxified_resource_url(data_dict)
            p.toolkit.c.resource['url'] = url
        iframe_src = "{}?{}".format(
            self.arcgis_webmap_viewer_url_embed,
            urllib.urlencode(self.webmap_viewer_embed_params)
        )
        p.toolkit.c.iframe_src = iframe_src


    def preview_template(self, context, data_dict):
        return 'wms.html'
