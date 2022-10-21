from typing import Dict, Union, Tuple, Type


class SerializerMappingMixin:
    serializer_mapping: Dict[Union[str, Tuple], Type] = {}

    def get_serializer_class(self):
        for action, serializer in self.serializer_mapping.items():
            if self.action == action or self.action in action:
                return serializer
        return self.serializer
