"""Functions which helps the locomotive engineer to keep track of the train."""

def get_list_of_wagons(*wagons):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return [*wagons]

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    a, b, c, *last = each_wagons_id
    
    return [c, *missing_wagons, *last, a, b]

def add_missing_stops(destination, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    destination['stops'] = [value for key, value in kwargs.items() if key.startswith('stop_')]
    return destination


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    combined_info = {**route , **more_route_information}
    return combined_info

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    [*row_1], [*row_2], [*row_3] = zip(*wagons_rows)
    ordered_rows = [row_1, row_2, row_3]
    
    return ordered_rows
