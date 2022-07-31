from xmlrpc.server import DocXMLRPCRequestHandler
import pyautogui as pag
import numpy as np
import matplotlib.pyplot as plt
import time

#import filter_function
start=time.time()
import numpy as np
from scipy import signal
times=0
m_drift_posi_x=0
m_posi_list_x=[]
m_posi_list_y=[]
m_posi_drift_list_x=[]
m_posi_drift_list_y=[]
m_posi_offset_list_x=[]
m_posi_offset_list_y=[]
samplerate=25600

def lowpass(x, samplerate, fp, fs, gpass, gstop):
    fp = 30   #通過域端周波数[Hz]
    fs = 95    #阻止域端周波数[Hz]
    gpass = 5      #通過域端最大損失[dB]
    gstop = 40      #阻止域端最小損失[dB]  
    fn = samplerate / 2                           #ナイキスト周波数
    wp = fp / fn                                  #ナイキスト周波数で通過域端周波数を正規化
    ws = fs / fn                                  #ナイキスト周波数で阻止域端周波数を正規化
    N, Wn = signal.buttord(wp, ws, gpass, gstop)  #オーダーとバターワースの正規化周波数を計算
    b, a = signal.butter(N, Wn, "low")            #フィルタ伝達関数の分子と分母を計算
    y = signal.filtfilt(b, a, x)                  #信号に対してフィルタをかける
    return y                                      #フィルタ後の信号を返す

def highpass(x, samplerate, fp, fs, gpass, gstop):
    fp = 95       #通過域端周波数[Hz]
    fs = 30       #阻止域端周波数[Hz]
    gpass = 5       #通過域端最大損失[dB]
    gstop = 40      #阻止域端最小損失[dB]
    fn = samplerate / 2                           #ナイキスト周波数
    wp = fp / fn                                  #ナイキスト周波数で通過域端周波数を正規化
    ws = fs / fn                                  #ナイキスト周波数で阻止域端周波数を正規化
    N, Wn = signal.buttord(wp, ws, gpass, gstop)  #オーダーとバターワースの正規化周波数を計算
    b, a = signal.butter(N, Wn, "high")           #フィルタ伝達関数の分子と分母を計算
    y = signal.filtfilt(b, a, x)                  #信号に対してフィルタをかける
    return y                                      #フィルタ後の信号を返す
while time.time()-start<5:
  #get mouse positon
  m_posi_x, m_posi_y = pag.position()
  m_posi_list_x.append(m_posi_x)
  m_posi_list_y.append(m_posi_y)
  dt=time.time()-start
  #ドリフト特性を付与したデータ
  m_posi_drift_list_x.append(m_posi_x+7.0*dt)
  m_posi_drift_list_y.append(m_posi_y+7.0*dt)
  #オフセット特性を付与したデータ
  m_posi_offset_list_x.append(m_posi_x+7)
  m_posi_offset_list_y.append(m_posi_y+7)
  times+=1

x=times/samplerate
print(times)
fp = 30       #通過域端周波数[Hz]
fs = 100       #阻止域端周波数[Hz]
gpass = 3       #通過域端最大損失[dB]
gstop = 40      #阻止域端最小損失[dB]
data_filt_x=lowpass(m_posi_drift_list_x,times-1,fp,fs,gpass,gstop)
data_filt_y=lowpass(m_posi_drift_list_y,times-1,fp,fs,gpass,gstop)
fp = 100       #通過域端周波数[Hz]
fs = 30       #阻止域端周波数[Hz]
gpass = 3       #通過域端最大損失[dB]
gstop = 40      #阻止域端最小損失[dB]
data_highpass_x=highpass(m_posi_offset_list_x,times-1,fp,fs,gpass,gstop)
data_highpass_y=highpass(m_posi_offset_list_x,times-1,fp,fs,gpass,gstop)
data_result_x=data_filt_x+data_highpass_x
data_result_y=data_filt_y+data_highpass_y

plt.plot(data_result_y,data_result_x,c='red')
plt.plot(m_posi_list_y,m_posi_list_x,c='black')
plt.show()