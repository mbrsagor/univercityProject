from enumchoicefield import ChoiceEnumclass ArticleStatus(ChoiceEnum):    PENDING = 'pending'    REVIEW = 'review'    PUBLISH = 'publish'    @classmethod    def get_choices(cls):        return [(_attr, _attr.value) for _attr in ArticleStatus]