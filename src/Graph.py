import abc


class Graph(abc.ABC):
    @abc.abstractmethod
    def add_vertex(self, v):
        pass

    @abc.abstractmethod
    def add_edge(self, v, w):
        pass

    @abc.abstractmethod
    def delete_vertex(self, i):
        pass

    @abc.abstractmethod
    def delete_edge(self, v, w):
        pass

    @abc.abstractmethod
    def edge_exists(self, v, w):
        pass

    @abc.abstractmethod
    def order(self):
        pass

    @abc.abstractmethod
    def edge_amount(self):
        pass

    @abc.abstractmethod
    def get_vertex(self, i):
        pass

    @abc.abstractmethod
    def get_adjacent_list(self, v):
        pass
