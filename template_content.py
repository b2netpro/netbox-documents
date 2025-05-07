from netbox.plugins import PluginTemplateExtension
from django.conf import settings
from .models import (
    SiteDocument,
    LocationDocument,
    DeviceDocument,
    DeviceTypeDocument,
    ModuleTypeDocument,
    CircuitDocument,
    VMDocument,
    CircuitProviderDocument,
)

plugin_settings = settings.PLUGINS_CONFIG.get('netbox_documents', {})

# ✅ Safe filter helper for all FK lookups
def safe_filter(model, field, obj):
    field_id = f"{field}_id"
    if hasattr(obj, field_id) and getattr(obj, field_id):
        return model.objects.filter(**{field_id: getattr(obj, field_id)})
    return []

class SiteDocumentList(PluginTemplateExtension):
    model = 'dcim.site'

    def left_page(self):
        obj = self.context.get('object')
        if plugin_settings.get('enable_site_documents') and plugin_settings.get('site_documents_location') == 'left':
            return self.render('netbox_documents/sitedocument_include.html', extra_context={
                'site_documents': safe_filter(SiteDocument, 'site', obj),
            })
        return ""

    def right_page(self):
        obj = self.context.get('object')
        if plugin_settings.get('enable_site_documents') and plugin_settings.get('site_documents_location') == 'right':
            return self.render('netbox_documents/sitedocument_include.html', extra_context={
                'site_documents': safe_filter(SiteDocument, 'site', obj),
            })
        return ""

class LocationDocumentList(PluginTemplateExtension):
    model = 'dcim.location'

    def left_page(self):
        obj = self.context.get('object')
        if plugin_settings.get('enable_location_documents') and plugin_settings.get('location_documents_location') == 'left':
            return self.render('netbox_documents/locationdocument_include.html', extra_context={
                'location_documents': safe_filter(LocationDocument, 'location', obj),
            })
        return ""

    def right_page(self):
        obj = self.context.get('object')
        if plugin_settings.get('enable_location_documents') and plugin_settings.get('location_documents_location') == 'right':
            return self.render('netbox_documents/locationdocument_include.html', extra_context={
                'location_documents': safe_filter(LocationDocument, 'location', obj),
            })
        return ""

class DeviceDocumentList(PluginTemplateExtension):
    model = 'dcim.device'

    def left_page(self):
        obj = self.context.get('object')
        if plugin_settings.get('enable_device_documents') and plugin_settings.get('device_documents_location') == 'left':
            return self.render('netbox_documents/devicedocument_include.html', extra_context={
                'device_documents': safe_filter(DeviceDocument, 'device', obj),
            })
        return ""

    def right_page(self):
        obj = self.context.get('object')
        if plugin_settings.get('enable_device_documents') and plugin_settings.get('device_documents_location') == 'right':
            return self.render('netbox_documents/devicedocument_include.html', extra_context={
                'device_documents': safe_filter(DeviceDocument, 'device', obj),
            })
        return ""

class DeviceTypeDocumentList(PluginTemplateExtension):
    model = 'dcim.devicetype'

    def left_page(self):
        obj = self.context.get('object')
        if plugin_settings.get('enable_device_type_documents') and plugin_settings.get('device_type_documents_location') == 'left':
            return self.render('netbox_documents/devicetypedocument_include.html', extra_context={
                'device_type_documents': safe_filter(DeviceTypeDocument, 'device_type', obj),
            })
        return ""

    def right_page(self):
        obj = self.context.get('object')
        if plugin_settings.get('enable_device_type_documents') and plugin_settings.get('device_type_documents_location') == 'right':
            return self.render('netbox_documents/devicetypedocument_include.html', extra_context={
                'device_type_documents': safe_filter(DeviceTypeDocument, 'device_type', obj),
            })
        return ""

class ModuleTypeDocumentList(PluginTemplateExtension):
    model = 'dcim.moduletype'

    def left_page(self):
        obj = self.context.get('object')
        if plugin_settings.get('enable_module_type_documents') and plugin_settings.get('module_type_documents_location') == 'left':
            return self.render('netbox_documents/moduletypedocument_include.html', extra_context={
                'module_type_documents': safe_filter(ModuleTypeDocument, 'module_type', obj),
            })
        return ""

    def right_page(self):
        obj = self.context.get('object')
        if plugin_settings.get('enable_module_type_documents') and plugin_settings.get('module_type_documents_location') == 'right':
            return self.render('netbox_documents/moduletypedocument_include.html', extra_context={
                'module_type_documents': safe_filter(ModuleTypeDocument, 'module_type', obj),
            })
        return ""

class CircuitDocumentList(PluginTemplateExtension):
    model = 'circuits.circuit'

    def left_page(self):
        obj = self.context.get('object')
        if plugin_settings.get('enable_circuit_documents') and plugin_settings.get('circuit_documents_location') == 'left':
            return self.render('netbox_documents/circuitdocument_include.html', extra_context={
                'circuit_documents': safe_filter(CircuitDocument, 'circuit', obj),
            })
        return ""

    def right_page(self):
        obj = self.context.get('object')
        if plugin_settings.get('enable_circuit_documents') and plugin_settings.get('circuit_documents_location') == 'right':
            return self.render('netbox_documents/circuitdocument_include.html', extra_context={
                'circuit_documents': safe_filter(CircuitDocument, 'circuit', obj),
            })
        return ""

class VMDocumentList(PluginTemplateExtension):
    model = 'virtualization.virtualmachine'

    def left_page(self):
        obj = self.context.get('object')
        if plugin_settings.get('enable_vm_documents') and plugin_settings.get('vm_documents_location') == 'left':
            return self.render('netbox_documents/vmdocument_include.html', extra_context={
                'vm_documents': safe_filter(VMDocument, 'vm', obj),
            })
        return ""

    def right_page(self):
        obj = self.context.get('object')
        if plugin_settings.get('enable_vm_documents') and plugin_settings.get('vm_documents_location') == 'right':
            return self.render('netbox_documents/vmdocument_include.html', extra_context={
                'vm_documents': safe_filter(VMDocument, 'vm', obj),
            })
        return ""

class CircuitProviderDocumentList(PluginTemplateExtension):
    model = 'circuits.provider'

    def left_page(self):
        obj = self.context.get('object')
        if plugin_settings.get('enable_circuit_provider_documents') and plugin_settings.get('circuit_provider_documents_location') == 'left':
            return self.render('netbox_documents/circuitproviderdocument_include.html', extra_context={
                'circuit_provider_documents': safe_filter(CircuitProviderDocument, 'provider', obj),
            })
        return ""

    def right_page(self):
        obj = self.context.get('object')
        if plugin_settings.get('enable_circuit_provider_documents') and plugin_settings.get('circuit_provider_documents_location') == 'right':
            return self.render('netbox_documents/circuitproviderdocument_include.html', extra_context={
                'circuit_provider_documents': safe_filter(CircuitProviderDocument, 'provider', obj),
            })
        return ""

template_extensions = [
    SiteDocumentList,
    LocationDocumentList,
    DeviceDocumentList,
    DeviceTypeDocumentList,
    ModuleTypeDocumentList,
    CircuitDocumentList,
    VMDocumentList,
    CircuitProviderDocumentList,
]

