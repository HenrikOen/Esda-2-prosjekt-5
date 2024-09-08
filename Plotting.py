import numpy as np
import matplotlib.pyplot as plt
import csv
import os



#Definin the file paths:
Amplitude_response_path    = "Malinger\\Amplitude_response.csv"
Voltage_with_RL_RK_path    = "Malinger\\V0=0.5_With_Ro_Ri.csv"
Voltage_without_RL_RK_path = "Malinger\\V0=0.5_Without_Ro_Ri.csv"
Voltage_max_amplitude_path = "Malinger\\V0=2_With_Ro_Ri.csv"



#Function for converting file to lists (oscilliscope):
def file_to_list(file, time_coloumn, Voltage1_column, Voltage2_column):
    Voltage1_list =[]
    Voltage2_list =[]
    time_list     = []
    n=0
    with open(file, 'r') as file:
        data=csv.reader(file)
        for row in data:
            
            if len(row)==0:
                continue
            elif not (row[0][0].isdigit()):
                continue
            time_list.append(float(row[time_coloumn]))
            Voltage1_list.append(float(row[Voltage1_column]))
            Voltage2_list.append(float(row[Voltage2_column]))

    return  time_list, Voltage1_list, Voltage2_list


#Defining function to convert csv file to lists (Amplitude response):
def file_to_list_Response(file, freq_column, magnetude_column):
    freq_list=[]
    magnetude_list=[]
    n=0
    with open(file, 'r') as file:
        data=csv.reader(file)
        for row in data:
            
            if len(row)==0:
                continue
            elif not (row[0][0].isdigit()):
                continue
            freq_list.append(float(row[freq_column]))
            magnetude_list.append(float(row[magnetude_column]))
        return freq_list, magnetude_list


Time_list_without_RL_RK, Voltage1_without_RL_RK, Voltage2_without_RL_RK = file_to_list(Voltage_without_RL_RK_path, 0, 1, 2)
Time_list_with_RL_RK, Voltage1_with_RL_RK, Voltage2_with_RL_RK          = file_to_list(Voltage_with_RL_RK_path, 0, 1, 2)
Time_list_max_amplitude, Voltage1_max_amplitude, Voltage2_max_amplitude = file_to_list(Voltage_max_amplitude_path, 0, 1, 2)
Frequency_list_input, Magnitude_list_input                              = file_to_list_Response(Amplitude_response_path, 0, 1)
Frequency_list_output, Magnitude_list_output                            = file_to_list_Response(Amplitude_response_path, 0, 2)
Frequency_list_output, frequency_list_output                            = file_to_list_Response(Amplitude_response_path, 0, 3)


#creating folder for graphs:
folder_path = 'Graphs'
os.makedirs(folder_path, exist_ok=True)

#Plottign and saving graphs:



# #With RL, RK:
# plt.figure()
# plt.plot(np.array(Time_list_with_RL_RK)*1000, np.array(Voltage2_with_RL_RK)*1000)
# plt.plot(np.array(Time_list_with_RL_RK)*1000, np.array(Voltage1_with_RL_RK)*1000)
# plt.title('Input and output signal, with RL, RK')
# plt.xlabel('Time [ms]')
# plt.ylabel('Magnitude [mV]')
# plt.legend(['Input signal', 'Output signal'])
# plt.grid()
# plt.savefig('Graphs\Signal_with_RL_RK.png')
# # plt.show()



# #Without RL, RK:
# plt.figure()
# plt.plot(np.array(Time_list_without_RL_RK)*1000, np.array(Voltage2_without_RL_RK)*1000-7625)
# plt.plot(np.array(Time_list_without_RL_RK)*1000, np.array(Voltage1_without_RL_RK)*1000)
# plt.title('Input and output signal, without RL, RK')
# plt.xlabel('Time [ms]')
# plt.ylabel('Magnitude [mV]')
# plt.legend(['Input signal', 'Output signal'])
# plt.grid()
# plt.savefig('Graphs\Signal_without_RL_RK.png')
# # plt.show()


# #Max ampitude:
# plt.figure()
# plt.plot(np.array(Time_list_max_amplitude)*1000, np.array(Voltage2_max_amplitude)*1000)
# plt.plot(np.array(Time_list_max_amplitude)*1000, np.array(Voltage1_max_amplitude)*1000)
# plt.title('Input and output signal, V0=V2')
# plt.xlabel('Time [ms]')
# plt.ylabel('Magnitude [mV]')
# plt.legend(['Input signal', 'Output signal'])
# plt.grid()
# plt.savefig('Graphs\Signal_Max_amplitude.png')
# # plt.show()


#Amplitude response:
plt.figure()
plt.semilogx(Frequency_list_output, Magnitude_list_output )
plt.semilogx(Frequency_list_input, Magnitude_list_input)


plt.title('Amplitude Response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')
plt.legend(['Output signal', 'Input signal'])
plt.grid()
# plt.show()
plt.savefig('Graphs\Amplitude_response.png')

plt.figure()
plt.semilogx(Frequency_list_output, frequency_list_output, color='blue' )
plt.title('Phase response')
plt.xlabel('Freqyency [Hz]')
plt.ylabel('Phase [\u00B0]')
plt.legend(['Output signal'])
plt.grid()

plt.savefig('Graphs\Phase_response.png')
plt.show()