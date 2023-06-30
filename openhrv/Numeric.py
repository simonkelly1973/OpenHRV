from openhrv.Time_t import Time_t

class Numeric:
    '''Class that stores all of the information of an OpenICE Numeric object'''

    def __init__(self):
        '''Initialises all of the fields of the Numeric object as empty strings or 0s'''

        self.unique_device_identifier = ""
        self.metric_id = ""
        self.vendor_metric_id = ""
        self.instance_id = 0
        self.unit_id = ""
        self.value = 0
        self.device_time = Time_t()
        self.presentation_time = Time_t()


    def clear(self):
        '''Clears all of the fields of the Numeric object back to the inital state'''

        self.unique_device_identifier = ""
        self.metric_id = ""
        self.vendor_metric_id = ""
        self.instance_id = 0
        self.unit_id = ""
        self.value = 0
        if self.device_time != None: self.device_time.clear()
        if self.presentation_time != None: self.presentation_time.clear()


    def update_fields(self, dictionary):
        '''Updates the fields of the Numeric object by taking in a dictionary of all of the required fields\n
            Required Fields:\n
            unique_device_identifier,\n
            metric_id,\n
            vendor_metric_id,\n
            instance_id,\n
            unit_id,\n
            value,\n
            device_time (Dictionary containing sec and nanosec),\n
            presentation_time'''
        
        self.unique_device_identifier = dictionary['unique_device_identifier']
        self.metric_id = dictionary['metric_id']
        self.vendor_metric_id = dictionary['vendor_metric_id']
        self.instance_id = dictionary['instance_id']
        self.unit_id = dictionary['unit_id']
        self.value = dictionary['value']
        self.device_time.update_fields(dictionary['device_time'])
        self.presentation_time.update_fields(dictionary['presentation_time'])

    def publish_fields(self):
        '''Returns a dictionary in a form that can be directly published to DDS'''

        publishing_dict = {}
        publishing_dict['unique_device_identifier'] = self.unique_device_identifier
        publishing_dict['metric_id'] = self.metric_id
        publishing_dict['vendor_metric_id'] = self.vendor_metric_id
        publishing_dict['instance_id'] = self.instance_id
        publishing_dict['unit_id'] = self.unit_id
        publishing_dict['value'] = self.value
        publishing_dict['device_time'] = self.device_time.publish_fields()
        publishing_dict['presentation_time'] = self.device_time.publish_fields()

        return publishing_dict