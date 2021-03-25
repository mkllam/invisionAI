# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import math
# Press the green button in the gutter to run the script.
"""
xA, yA, w, h, theta
"""

if __name__ == '__main__':
    """for the sake of time, will use hardcoded parameters instead of arguments"""
    xA = 10
    yA = 20
    w = h = 5
    theta = 20  #  Assume given in degrees so convert to radians.
    theta = theta/180 * math.pi
    xy = pd.read_csv('data.csv').to_numpy()
    print(xy)
    flag = []
    for i in xy:
        # x = i[0]  ;  y = i[1]
        # src: https://gamedev.stackexchange.com/questions/79765/how-do-i-convert-from-the-global-coordinate-space-to-a-local-space
        relativeX = (i[0]-xA)*math.cos(theta) + (i[1]-yA)*math.sin(theta)
        relativeY = -(i[0]-xA)*math.sin(theta) + (i[1]-yA)*math.cos(theta)
        flag.append(0 < relativeX < w and 0 < relativeY < h)
    print(flag)
    # https://datatofish.com/export-dataframe-to-csv/
    df = pd.DataFrame(flag, columns=['Flag'])
    df.to_csv('result.csv', index=False, header=True)





