# coding=utf-8
# The cding line above must remain for the long dash to work.


KBDH-VN transcripting python scriipt

# Inputs: 
#     source : array with local text fie names
#     chapter_labels: array with names of the label tag (what to add in the first line for ren'py script)
#     targets : array with names of the output files
#    
# Those three arrays must be of the same length.
    
    
    

import re 

sources = [ "kbdh00.txt", 
            "kbdh01.txt", 
            "kbdh02.txt", 
            "kbdh03.txt", 
            "kbdh04.txt", 
            "kbdh05.txt", 
            "kbdh06.txt", 
            "kbdh07.txt", 
            "kbdh08.txt", 
            "kbdh09.txt", 
            "kbdh10.txt", 
            "kbdh11.txt", 
            "kbdh12.txt", 
            "kbdh13.txt", 
            "kbdh14.txt", 
            "kbdh15.txt", 
            "kbdh16.txt", 
            "kbdh17.txt", 
            "kbdh18.txt", 
            "kbdh19.txt", 
            "kbdh20.txt", 
            "kbdh21.txt", 
            "kbdh22.txt", 
            "kbdh23.txt", 
            "kbdh24.txt", 
            "kbdh25.txt", 
            "kbdh26.txt", 
            "kbdh27.txt", 
            "kbdh28.txt", 
            "kbdh29.txt", 
            "kbdh30.txt", 
            "kbdh31.txt", 
            "kbdh32.txt", 
            "kbdh33.txt", 
            "kbdh34.txt", 
            "kbdh35.txt", 
            "kbdh36.txt", 
            "kbdh37.txt", 
            "kbdh38.txt", 
            "kbdh39.txt", 
            "kbdh40.txt", 
            "kbdh41.txt", 
            "kbdh42.txt", 
            "kbdh43.txt", 
            "kbdh44.txt", 
            "kbdh45.txt", 
            "kbdh46.txt", 
            "kbdh47.txt", 
            "kbdh48.txt", 
            "kbdh49.txt", 
            "kbdh50.txt", 
            "kbdh51.txt"]

chapter_labels = [  "ch000_IMRP", 
                    "ch001_AO_1", 
                    "ch002_AO_2", 
                    "ch003_SF_1", 
                    "ch004_SF_2", 
                    "ch005_SF_3", 
                    "ch006_HAB_1", 
                    "ch007_HAB_2", 
                    "ch008_Fi_1", 
                    "ch009_Fi_2", 
                    "ch010_HAB_3", 
                    "ch011_HAB_4", 
                    "ch012_HAB_5", 
                    "ch013_Fi_3", 
                    "ch014_Fi_4", 
                    "ch015_Fa_1", 
                    "ch016_Fa_2", 
                    "ch017_Fa_3", 
                    "ch018_Fa_4", 
                    "ch019_GU_1", 
                    "ch020_GU_2", 
                    "ch021_GU_3", 
                    "ch022_GU_4", 
                    "ch023_GU_5", 
                    "ch024_IC_1", 
                    "ch025_IC_2", 
                    "ch026_IC_3", 
                    "ch027_IC_4", 
                    "ch028_IC_5", 
                    "ch029_TL_1", 
                    "ch030_TL_2", 
                    "ch031_TL_3", 
                    "ch032_TL_4", 
                    "ch033_TL_5", 
                    "ch034_CBS_1", 
                    "ch035_CBS_2", 
                    "ch036_CBS_3", 
                    "ch037_CBS_4", 
                    "ch038_CBS_5", 
                    "ch039_SB_1", 
                    "ch040_SB_2", 
                    "ch041_SB_3", 
                    "ch042_SB_4", 
                    "ch043_SB_5", 
                    "ch044_OB_1", 
                    "ch045_OB_2", 
                    "ch046_OB_3", 
                    "ch047_OB_4", 
                    "ch048_OB_5", 
                    "ch049_OB_6", 
                    "ch050_OB_7", 
                    "ch051_LL_1"]

targets = [ "chapter000_IMRP.rpy", 
            "chapter001_AO-1.rpy", 
            "chapter002_AO-2.rpy", 
            "chapter003_SF-1.rpy", 
            "chapter004_SF-2.rpy", 
            "chapter005_SF-3.rpy", 
            "chapter006_HAB-1.rpy", 
            "chapter007_HAB-2.rpy", 
            "chapter008_Fi-1.rpy", 
            "chapter009_Fi-2.rpy", 
            "chapter010_HAB-3.rpy", 
            "chapter011_HAB-4.rpy", 
            "chapter012_HAB-5.rpy", 
            "chapter013_Fi-3.rpy", 
            "chapter014_Fi-4.rpy", 
            "chapter015_Fa-1.rpy", 
            "chapter016_Fa-2.rpy", 
            "chapter017_Fa-3.rpy", 
            "chapter018_Fa-4.rpy", 
            "chapter019_GU-1.rpy", 
            "chapter020_GU-2.rpy", 
            "chapter021_GU-3.rpy", 
            "chapter022_GU-4.rpy", 
            "chapter023_GU-5.rpy", 
            "chapter024_IC-1.rpy", 
            "chapter025_IC-2.rpy", 
            "chapter026_IC-3.rpy", 
            "chapter027_IC-4.rpy", 
            "chapter028_IC-5.rpy", 
            "chapter029_TL-1.rpy", 
            "chapter030_TL-2.rpy", 
            "chapter031_TL-3.rpy", 
            "chapter032_TL-4.rpy", 
            "chapter033_TL-5.rpy", 
            "chapter034_CBS-1.rpy", 
            "chapter035_CBS-2.rpy", 
            "chapter036_CBS-3.rpy", 
            "chapter037_CBS-4.rpy", 
            "chapter038_CBS-5.rpy", 
            "chapter039_SB-1.rpy", 
            "chapter040_SB-2.rpy", 
            "chapter041_SB-3.rpy", 
            "chapter042_SB-4.rpy", 
            "chapter043_SB-5.rpy", 
            "chapter044_OB-1.rpy", 
            "chapter045_OB-2.rpy", 
            "chapter046_OB-3.rpy", 
            "chapter047_OB-4.rpy", 
            "chapter048_OB-5.rpy", 
            "chapter049_OB-6.rpy", 
            "chapter050_OB-7.rpy", 
            "chapter051_LL-1.rpy"]
            
for i in range(min(len(sources), len(targets))): # To iterate through all files
# for i in [len(sources)-1]: # for last element of array only
    #label = chapter_labels[i]
    file_source = open(sources[i], 'r')
    file_target = open(targets[i], 'w')
    
    text = file_source.read()
    
    text = re.sub(r"\A[^*]*\* \* \*[^*]*\* \* \*", "", text, 1)    
    
    text = text.replace('--', '—')
    while text.find('_') != text.rfind('_'):
        text = text.replace('_', '{i}', 1)
        text = text.replace('_', '{/i}', 1)
    
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
#    text = re.sub(r'(?<=(,|;|\.|\!|\?))"\n', '" \n', text)
#    text = re.sub(r"(?<=(,|;|\.|\!|\?))\n", " \n", text)
    text = text.replace(r'"', r'\"')
    
    text = re.sub(r"\n+", r'"\n    "', text)
    
    text = 'label {0}:\n    "{1}"\n'.format(chapter_labels[i], text)
    text = text.replace('\n    ""', '')
    
    file_target.write(text)
    
    
