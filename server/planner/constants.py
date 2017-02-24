class UserRoleType(object):
    ORGANIZER = 1
    IDEA_COLLECTOR = 2
    GIFT_BUYER_ONLINE = 3
    GIFT_BUYER_OFFLINE = 4
    GIFT_WRAPPER = 5

    @classmethod
    def get_choices(cls):
        return (
            (cls.ORGANIZER, USER_ROLE_TITLE[cls.ORGANIZER]),
            (cls.IDEA_COLLECTOR, USER_ROLE_TITLE[cls.IDEA_COLLECTOR]),
            (cls.GIFT_BUYER_ONLINE, USER_ROLE_TITLE[cls.GIFT_BUYER_ONLINE]),
            (cls.GIFT_BUYER_OFFLINE, USER_ROLE_TITLE[cls.GIFT_BUYER_OFFLINE]),
            (cls.GIFT_WRAPPER, USER_ROLE_TITLE[cls.GIFT_WRAPPER]),
        )

USER_ROLE_TITLE = {
    UserRoleType.ORGANIZER: 'Organizer',
    UserRoleType.IDEA_COLLECTOR: 'Idea collector',
    UserRoleType.GIFT_BUYER_ONLINE: 'Gift buyer (online)',
    UserRoleType.GIFT_BUYER_OFFLINE: 'Gift buyer (offline)',
    UserRoleType.GIFT_WRAPPER: 'Gift wrapper',
}

USER_ROLE_DESCRIPTION = {
    UserRoleType.ORGANIZER: 'It\'s your turn to be king/queen of your birthday party. '
    'Collect ideas for the date, venue and activities you want to do to '
    'celebrate this special day. When you decide on everything, send out an '
    'invitation.',
    UserRoleType.IDEA_COLLECTOR: 'Choose the most voted idea for each of the '
    'birthday boys and gals and prepare final list of gifts.',
    UserRoleType.GIFT_BUYER_ONLINE: 'Your job is to check final list of gifts '
    'and go pick them up in local stores.',
    UserRoleType.GIFT_BUYER_OFFLINE: 'Check final list of gifts to see if '
    'there are any gifts that should be purchased online and buy them.',
    UserRoleType.GIFT_WRAPPER: 'You\'ve been chosen to make gifts pretty and '
    'special. Find nice gift cards and bags or wrapping paper for each of the '
    'birthday boys/gals.',
}
