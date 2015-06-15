from jinja2.utils import soft_unicode

def get_subnets(value, tag_key, tag_value, return_type='id'):
    # return all subnets that match
    subnets = []
    for item in value:
      for key, value in item['resource_tags'].iteritems():
        if key == tag_key and value == tag_value:
          subnets.append(item[return_type])
            
    return subnets


class FilterModule(object):
    ''' Ansible core jinja2 filters '''

    def filters(self):
        return {
            'get_subnets': get_subnets,
        }
