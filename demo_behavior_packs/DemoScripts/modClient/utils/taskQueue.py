# -*- coding: utf-8 -*-


class TaskQueue(object):
    def __init__(self):
        self._task_queue = []

    def add_task(self, task):
        self._task_queue.append(task)

    def tick(self):
        for task in self._task_queue:
            if task.isFinished:
                self._task_queue.remove(task)
            else:
                task.run()
