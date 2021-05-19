# -*- coding: utf-8 -*-


class Task(object):
    def __init__(self, task, delay, repeat, *args, **kwargs):
        self.__task = task
        self.__delay = delay
        self.__repeat_times = repeat
        self.__args = args
        self.__kwargs = kwargs
        self.__finished = False

    @property
    def isFinished(self):
        return self.__finished

    def run(self):
        if self.__delay > 0:
            self.__delay -= 1
        else:
            if self.__repeat_times > 0:
                self.__task(self.__args, self.__kwargs)
                self.__repeat_times -= 1
            else:
                self.__finished = True







