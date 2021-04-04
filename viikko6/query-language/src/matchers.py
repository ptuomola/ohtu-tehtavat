class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)
        return player_value >= self._value

class Not:
    def __init__(self, condition):
        self._condition = condition
    
    def matches(self, player):
        return not self._condition.matches(player)

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class All:
    def matches(self, player):
        return True

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True
        
        return False    

class QueryBuilder:
    def __init__(self):
        self._matcher = All()

    def playsIn(self, team):
        self._matcher = And(PlaysIn(team), self._matcher)
        return self

    def hasAtLeast(self, value, attr):
        self._matcher = And(HasAtLeast(value, attr), self._matcher)
        return self

    def hasFewerThan(self, value, attr):
        self._matcher = And(HasFewerThan(value, attr), self._matcher)
        return self

    def oneOf(self, *matchers):
        self._matcher = Or(*matchers)
        return self

    def build(self):
        matcher = self._matcher
        self._matcher = All()
        return matcher
