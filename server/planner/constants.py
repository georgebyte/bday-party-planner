class UserRoleType(object):
    ORGANIZER = 1
    IDEA_COLLECTOR = 2
    PRESENT_BUYER_ONLINE = 3
    PRESENT_BUYER_OFFLINE = 4
    PRESENT_WRAPPER = 5

    @classmethod
    def get_choices(cls):
        return (
            (cls.ORGANIZER, 'Organizer'),
            (cls.IDEA_COLLECTOR, 'Idea collector'),
            (cls.PRESENT_BUYER_ONLINE, 'Gift buyer (online)'),
            (cls.PRESENT_BUYER_OFFLINE, 'Gift buyer (offline)'),
            (cls.PRESENT_WRAPPER, 'Gift wrapper'),
        )
