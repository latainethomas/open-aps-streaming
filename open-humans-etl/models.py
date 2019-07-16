
from dateutil.parser import parse
from datetime import datetime
from functools import reduce
import operator
import json


class Entry:

    def __init__(self, entity):

        self.app_id = entity['app_id']
        self.id = entity['_id']

        self.sgv = entity.get('sgv')
        self.direction = entity.get('direction')
        self.device = entity['device'].replace('\x00', '') if 'device' in entity else None
        self.type = entity.get('type')
        self.rssi = entity.get('rssi')
        self.rawbg = entity.get('rawbg')
        self.trend = entity['trend'] if 'trend' in entity else entity.get('trend_arrow')
        self.glucose = entity.get('glucose')
        self.mbg = entity.get('mbg')
        self.delta = entity.get('delta')
        self.filtered = entity.get('filtered')
        self.unfiltered = entity.get('unfiltered')
        self.noise = entity.get('noise')
        self.scale = entity.get('scale')
        self.slope = entity.get('slope')
        self.intercept = entity.get('intercept')

        self.raw_json = json.dumps(entity)

        self.system_time = entity['system_time'] if 'system_time' in entity else entity.get('sysTime')
        self.date = datetime.fromtimestamp(entity['date']/1000).strftime('%Y-%m-%d %H:%M:%S')

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        pass


class Treatment:

    def __init__(self, entity):

        self.app_id = entity['app_id']
        self.id = entity['_id'] if '_id' in entity else entity['id'] if 'id' in entity else entity['uuid']
        self.event_type = entity.get('eventType')
        self.timestamp = self._parse_date(entity.get('timestamp'))

        self.insulin = entity.get('insulin')
        self.carbs = entity.get('carbs')
        self.protein = entity.get('protein') if entity.get('protein') != '' else None
        self.fat = entity.get('fat') if entity.get('fat') != '' else None
        self.glucose = entity.get('glucose')
        self.glucose_type = entity.get('glucoseType')
        self.food_type = entity.get('foodType')

        self.temp = entity.get('temp')
        self.rate = entity.get('rate')
        self.duration = entity.get('duration')
        self.units = entity.get('units')
        self.amount = entity.get('amount')
        self.absolute = entity.get('absolute')
        self.bolus = json.dumps(entity.get('bolus'))
        self.boluscalc = json.dumps(entity.get('boluscalc'))
        self.medtronic = entity.get('medtronic')

        self.type = entity.get('type')
        self.absorption_time = entity.get('absorptionTime')
        self.unabsorbed = entity.get('unabsorbed')
        self.ratio = entity.get('ratio')
        self.wizard = json.dumps(entity.get('wizard'))
        self.target_top = entity.get('targetTop')
        self.target_bottom = entity.get('targetBottom')
        self.fixed = entity.get('fixed')
        self.programmed = entity.get('programmed')

        self.reason = entity.get('reason')
        self.notes = entity.get('notes')

        self.raw_json = json.dumps(entity)

        self.entered_by = entity.get('enteredBy')
        self.created_at = entity.get('created_at')

    @staticmethod
    def _parse_date(date):

        if not date:
            return date
        elif isinstance(date, int):
            return str(datetime.fromtimestamp(float(date) / 1000))
        else:
            return str(parse(date))

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        pass


class Profile:

    def __init__(self, entity):

        self.app_id = entity['app_id']
        self.id = entity['_id']
        self.default_profile = entity.get('defaultProfile')
        self.mills = entity.get('mills')
        self.units = entity.get('units')

        self.store = json.dumps(entity.get('store'))
        self.loop_settings = json.dumps(entity.get('loopSettings'))

        self.raw_json = json.dumps(entity)

        self.start_date = entity.get('startDate')
        self.created_at = entity.get('created_at')

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        pass


class DeviceStatus:

    def __init__(self, entity):

        self.entity = entity

        self.app_id = entity['app_id']
        self.id = entity['_id']
        self.device = entity.get('device')

        self.pump_id = self._extract(['pump', 'pumpID'])
        self.pump_bolusing = self._extract(['pump', 'bolusing']) if 'pump' in entity and 'bolusing' in entity['pump'] else self._extract(['pump', 'status', 'bolusing'])
        self.pump_suspended = self._extract(['pump', 'suspended']) if 'pump' in entity and 'suspended' in entity['pump'] else self._extract(['pump', 'status', 'suspended'])
        self.pump_model = self._extract(['pump', 'model'])

        self.loop_cob = self._extract(['loop', 'cob', 'cob'])
        self.loop_iob = self._extract(['loop', 'iob', 'iob'])
        self.loop_version = self._extract(['loop', 'version'])
        self.loop_failure_reason = self._extract(['loop', 'failureReason'])

        self.snooze = entity.get('snooze')
        self.override_active = self._extract(['override', 'active'])

        self.raw_json = json.dumps(entity)

        self.created_at = entity['created_at']

        del self.entity

    def _extract(self, keys):
        try:
            return reduce(operator.getitem, keys, self.entity)
        except (KeyError,TypeError):
            return None

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        pass


class DeviceStatusMetric:

    def __init__(self, entity):

        self.entity = entity

        self.device_status_id = entity['device_status_id']

        self.iob_iob = self._extract(['iob', 'iob'])
        self.iob_activity = self._extract(['iob', 'activity'])
        self.iob_basal_iob = self._extract(['iob', 'basaliob'])
        self.iob_bolus_iob = self._extract(['iob', 'bolusiob'])
        self.iob_net_basal_insulin = self._extract(['iob', 'netbasalinsulin'])
        self.iob_bolus_insulin = self._extract(['iob', 'bolusinsulin'])
        self.iob_timestamp = self._extract(['iob', 'timestamp'])

        self.suggested_temp = self._extract(['suggested', 'temp'])
        self.suggested_bg = self._extract(['suggested', 'bg'])
        self.suggested_tick = self._extract(['suggested', 'tick'])
        self.suggested_eventual_bg = self._extract(['suggested', 'eventualBG'])
        self.suggested_insulin_req = self._extract(['suggested', 'insulinReq'])
        self.suggested_reservoir = self._extract(['suggested', 'reservoir'])
        self.suggested_cob = self._extract(['suggested', 'COB'])
        self.suggested_iob = self._extract(['suggested', 'IOB'])

        self.enacted_temp = self._extract(['enacted', 'temp'])
        self.enacted_bg = self._extract(['enacted', 'bg'])
        self.enacted_tick = self._extract(['enacted', 'tick'])
        self.enacted_eventual_bg = self._extract(['enacted', 'eventualBG'])
        self.enacted_insulin_req = self._extract(['enacted', 'insulinReq'])
        self.enacted_reservoir = self._extract(['enacted', 'reservoir'])
        self.enacted_cob = self._extract(['enacted', 'COB'])
        self.enacted_iob = self._extract(['enacted', 'IOB'])
        self.enacted_duration = self._extract(['enacted', 'duration'])
        self.enacted_rate = self._extract(['enacted', 'rate'])

        self.raw_json = json.dumps(entity)

        self.enacted_timestamp = self._extract(['enacted', 'timestamp'])

        del self.entity

    def _extract(self, keys):
        try:
            return reduce(operator.getitem, keys, self.entity)
        except (KeyError,TypeError):
            return None

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        pass
