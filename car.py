from shapes import Paper, Triangle, Rectangle, Oval
import pandas as pd


df = pd.read_csv(
    'Dataset/PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4/Group_349.csv')
df[['_g_Infrastructure_CCR_NET_NetRunnablesClass_m_rteInputData_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem._m_camData._m_objects._m_value._0_._m_dx',
    '_g_Infrastructure_CCR_NET_NetRunnablesClass_m_rteInputData_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem._m_camData._m_objects._m_value._0_._m_dy']]

# Center
a = 300
b = 300
c = 300
d = 250
# Colors
sensorColor = "light coral"

paper = Paper()


def Car():
    body = Rectangle()
    bodyBlind1 = Rectangle()
    bodyBlind2 = Rectangle()
    cam = Triangle()
    s1 = Triangle()
    s2 = Triangle()
    s3 = Triangle()
    s4 = Triangle()

    body.set_param(100, 200, a, b, "blue")
    bodyBlind1.set_param(a-250, b-180, a-90, b, "red")
    bodyBlind2.set_param(a-250, b-180, a+90, b, "red")
    # rect1.set_x(0)
    # rect1.set_y(0)

    circ1 = Oval()

    circ1.set_param(20, 20, c, d, "black")

    # trian.draw()

    # body.draw()
    # bodyBlind1.draw()
    # bodyBlind2.draw()

    circ1.draw()

    cam.draw(a, b-178.26, a-50, b-220, a+50, b-220, "light green")
    s1.draw(a-73.8, b-76.64, a-73.8, b-200, a-200, b-76.64, sensorColor)
    s2.draw(a+73.8, b-76.64, a+73.8, b-200, a+200, b-76.64, sensorColor)
    s3.draw(a+62.86, b+347.38, a+62.86, b+500, a+200, b+347.38, sensorColor)
    s4.draw(a-62.86, b+347.38, a-62.86, b+500, a-200, b+347.38, sensorColor)


def Objects():
    obj1 = Oval()

    x = 0
    y = 0

    print('x')
    for row in range(0, 29872):
        dx = df['_g_Infrastructure_CCR_NET_NetRunnablesClass_m_rteInputData_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem._m_camData._m_objects._m_value._0_._m_dx'].iloc[row]
        dy = df['_g_Infrastructure_CCR_NET_NetRunnablesClass_m_rteInputData_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem._m_camData._m_objects._m_value._0_._m_dy'].iloc[row]
        x = dx/10
        y = dy/10
        obj1.set_param(5, 5, x, y, "blue")

        obj1.draw()
    '''
    print('y')
    for row in range(0, 50):
        dy = df['_g_Infrastructure_CCR_NET_NetRunnablesClass_m_rteInputData_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem._m_camData._m_objects._m_value._0_._m_dy'].iloc[row]
        
    '''


if(((185 <= c <= 235) and (240 <= d < 360)) or ((365 <= c <= 415) and (240 <= d < 360))):
    print("blind spot")


Car()

Objects()

paper.display()
