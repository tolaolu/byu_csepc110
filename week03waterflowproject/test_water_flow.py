from pytest import approx
import pytest

def test_water_column_height():

    from water_flow import water_column_height

    # Call the water_column_height function and verify that it returns a float.
    height = water_column_height(10, 4)
    assert isinstance(height, float), "water_column_height function must return a float"

    
    assert water_column_height(0.0, 0.0) == approx(0.0)
    assert water_column_height(0.0, 10.0) == approx(7.5)
    assert water_column_height(25.0, 0.0) == approx(25.0)
    assert water_column_height(48.3, 12.8) == approx(57.9)
    
def test_pressure_gain_from_water_height():
    from water_flow import pressure_gain_from_water_height
    
    # Call the pressure_gain_from_water_height function and verify that it returns a float.
    pressure = pressure_gain_from_water_height(10)
    assert isinstance(pressure, float), "pressure_gain_from_water_height function must return a float"

    assert pressure_gain_from_water_height(0.0) == approx(0.0, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)
    
def test_pressure_loss_from_pipe():
    
    from water_flow import pressure_loss_from_pipe

    # Call the pressure_loss_from_pipe function and verify that it returns a float.
    loss = pressure_loss_from_pipe(0.28687, 10, 0.013, 1.65)
    assert isinstance(loss, float), "pressure_loss_from_pipe function must return a float"

    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == approx(0.0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == approx(0.0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == approx(0.0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)

def test_pressure_loss_from_fittings():
    
    from water_flow import pressure_loss_from_fittings

    # Call the pressure_loss_from_fittings function and verify that it returns a float.
    loss = pressure_loss_from_fittings(1.65, 10)
    assert isinstance(loss, float), "pressure_loss_from_fittings function must return a float"

    assert pressure_loss_from_fittings(0.00, 3) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)

def test_reynolds_number():
    
    from water_flow import reynolds_number

    # Call the reynolds_number function and verify that it returns a float.
    number = reynolds_number(0.28687, 1.65)
    assert isinstance(number, float), "reynolds_number function must return a float"

    assert reynolds_number(0.048692, 0.00) == approx(0.0, abs=1)
    assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    assert reynolds_number(0.286870, 1.65) == approx(471729, abs=1)
    assert reynolds_number(0.286870, 1.75) == approx(500318, abs=1)

def test_pressure_loss_from_pipe_reduction():
    
    from water_flow import pressure_loss_from_pipe_reduction

    # Call the pressure_loss_from_pipe_reduction function and verify that it returns a float.
    loss = pressure_loss_from_pipe_reduction(0.28687, 1.65, 1000, 0.048692)
    assert isinstance(loss, float), "pressure_loss_from_pipe_reduction function must return a float"

    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])