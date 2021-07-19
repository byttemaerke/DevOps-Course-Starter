class ViewModel:
    def __init__(self, tasks):
        self._tasks = tasks

    @property
    def to_do_tasks(self):
        return [task for task in self._tasks if task.status == 'To Do']

    @property
    def doing_tasks(self):
        return [task for task in self._tasks if task.status == 'Doing']

    @property
    def done_tasks(self):
        return [task for task in self._tasks if task.status == 'Done']

    @property
    def should_show_all_done_tasks(self):
        return len(self.done_tasks) < 5

    @property
    def recent_done_tasks(self):
        return [task for task in self.done_tasks if task.modified_today()]

    @property
    def older_done_tasks(self):
        return [task for task in self.done_tasks if task.modified_before_today()]