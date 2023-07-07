import pandas as pd
import pytest
from utils.compare import compare_day_night_demand

def test_course_exists():
    data = {
        'Course': ['Engenharia Civil - Diurno', 'Administração - Noturno'],
        'Demand': [5, 2]
    }
    df = pd.DataFrame(data)
    result = compare_day_night_demand(df, 'Medicina')
    assert result == 'Course not found', "Test failed"

def test_compare_day_night_demand_no_day_course():
    data = {
        'Course': ['Administração - Noturno'],
        'Demand': [2]
    }
    df = pd.DataFrame(data)
    result = compare_day_night_demand(df, 'Administração')
    assert result == 'Day course not found', "Test failed"

def test_compare_day_night_demand_no_night_course():
    data = {
        'Course': ['Administração - Diurno'],
        'Demand': [2]
    }
    df = pd.DataFrame(data)
    result = compare_day_night_demand(df, 'Administração')
    assert result == 'Night course not found', "Test failed"

def test_compare_day_night_demand():
    data = {
        'Course': ['Administração - Diurno', 'Administração - Noturno'],
        'Demand': [3, 2]
    }
    df = pd.DataFrame(data)
    result = compare_day_night_demand(df, 'Administração')
    assert result == 'Day course has higher demand', "Test failed"

def test_compare_night_day_demand():
    data = {
        'Course': ['Administração - Diurno', 'Administração - Noturno'],
        'Demand': [2, 3]
    }
    df = pd.DataFrame(data)
    result = compare_day_night_demand(df, 'Administração')
    assert result == 'Night course has higher demand', "Test failed"

def test_same_demand():
    data = {
        'Course': ['Administração - Diurno', 'Administração - Noturno'],
        'Demand': [2, 2]
    }
    df = pd.DataFrame(data)
    result = compare_day_night_demand(df, 'Administração')
    assert result == 'Same demand', "Test failed"
