from datetime import date, datetime

class Task:
    def __init__(self, id, name, last_modified, status):
        self.id= id
        self.name = name
        self.last_modified = last_modified
        self.status = status
    
    @classmethod
    def fromTrelloCard(cls, card, list):
        return cls(
            card['id'],
            card['name'],
            datetime.strptime(card['dateLastActivity'], '%Y-%m-%dT%H:%M:%S.%fZ'),
            list['name']
        )
    
    def modified_today(self):
        return self.last_modified.date() == date.today()
    
    def modified_before_today(self):
        return self.last_modified.date() < date.today()
    
    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, status: {self.status}, last_modified: {self.last_modified}"
    
    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Task):
            return False
        
        return self.id == o.id \
            and self.name == o.name \
            and self.status == o.status \
            and self.last_modified == o.last_modified
