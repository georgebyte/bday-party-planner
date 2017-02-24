class UserRoleType(object):
    ORGANIZER = 1
    IDEA_COLLECTOR = 2
    GIFT_BUYER_ONLINE = 3
    GIFT_BUYER_OFFLINE = 4
    GIFT_WRAPPER = 5

    @classmethod
    def get_choices(cls):
        return (
            (cls.ORGANIZER, 'Organizer'),
            (cls.IDEA_COLLECTOR, 'Idea collector'),
            (cls.GIFT_BUYER_ONLINE, 'Gift buyer (online)'),
            (cls.GIFT_BUYER_OFFLINE, 'Gift buyer (offline)'),
            (cls.GIFT_WRAPPER, 'Gift wrapper'),
        )
