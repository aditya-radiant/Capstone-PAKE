# -*- coding: utf-8 -*-
"""Copy of revisi

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cncjWGRUUX93w7WjuKhFWo-4HTaZBON6
"""

import os
import zipfile
import random
import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from shutil import copyfile
import shutil

#shutil.rmtree('/tmp/datasets')

from google.colab import drive
drive.mount('/content/drive')

local_zip = '/content/drive/MyDrive/mobil.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/tmp')
zip_ref.close()

print(len(os.listdir('/tmp/mobil/86')))
print(len(os.listdir('/tmp/mobil/C-HR Hybrid')))
print(len(os.listdir('/tmp/mobil/C-Hr')))
print(len(os.listdir('/tmp/mobil/Hi-Max')))
print(len(os.listdir('/tmp/mobil/HiAce')))
print(len(os.listdir('/tmp/mobil/Karimun Wagon R')))
print(len(os.listdir('/tmp/mobil/Raize')))
print(len(os.listdir('/tmp/mobil/Terios')))
print(len(os.listdir('/tmp/mobil/Xenia')))
print(len(os.listdir('/tmp/mobil/agya')))
print(len(os.listdir('/tmp/mobil/all new carry pick up')))
print(len(os.listdir('/tmp/mobil/almaz')))
print(len(os.listdir('/tmp/mobil/alphard')))
print(len(os.listdir('/tmp/mobil/apv arena')))
print(len(os.listdir('/tmp/mobil/avanza')))
print(len(os.listdir('/tmp/mobil/ayla')))
print(len(os.listdir('/tmp/mobil/baleno')))
print(len(os.listdir('/tmp/mobil/calya')))
print(len(os.listdir('/tmp/mobil/camry')))
print(len(os.listdir('/tmp/mobil/camry hybrid')))
print(len(os.listdir('/tmp/mobil/confero')))
print(len(os.listdir('/tmp/mobil/corolla altis')))
print(len(os.listdir('/tmp/mobil/corolla altis hybrid')))
print(len(os.listdir('/tmp/mobil/corolla cross')))
print(len(os.listdir('/tmp/mobil/cortez')))
print(len(os.listdir('/tmp/mobil/ertiga')))
print(len(os.listdir('/tmp/mobil/formo')))
print(len(os.listdir('/tmp/mobil/fortuner')))
print(len(os.listdir('/tmp/mobil/gran max mb')))
print(len(os.listdir('/tmp/mobil/gran max pickup')))
print(len(os.listdir('/tmp/mobil/hilux d cab')))
print(len(os.listdir('/tmp/mobil/hilux s cab')))
print(len(os.listdir('/tmp/mobil/ignis')))
print(len(os.listdir('/tmp/mobil/jimny')))
print(len(os.listdir('/tmp/mobil/kijang innova')))
print(len(os.listdir('/tmp/mobil/land cruiser')))
print(len(os.listdir('/tmp/mobil/luxio')))
print(len(os.listdir('/tmp/mobil/rocky')))
print(len(os.listdir('/tmp/mobil/rush')))
print(len(os.listdir('/tmp/mobil/sienta')))
print(len(os.listdir('/tmp/mobil/sigra')))
print(len(os.listdir('/tmp/mobil/sirion')))
print(len(os.listdir('/tmp/mobil/supra')))
print(len(os.listdir('/tmp/mobil/vellfire')))
print(len(os.listdir('/tmp/mobil/veloz')))
print(len(os.listdir('/tmp/mobil/venturer')))
print(len(os.listdir('/tmp/mobil/vios')))
print(len(os.listdir('/tmp/mobil/voxy')))
print(len(os.listdir('/tmp/mobil/yaris')))

try:
    os.mkdir('/tmp/datasets')
    os.mkdir('/tmp/datasets/training')
    os.mkdir('/tmp/datasets/testing')
    os.mkdir('/tmp/datasets/training/86')
    os.mkdir('/tmp/datasets/training/C-HR Hybrid')
    os.mkdir('/tmp/datasets/training/C-Hr')
    os.mkdir('/tmp/datasets/training/Hi-Max')
    os.mkdir('/tmp/datasets/training/HiAce')
    os.mkdir('/tmp/datasets/training/Karimun Wagon R')
    os.mkdir('/tmp/datasets/training/Raize')
    os.mkdir('/tmp/datasets/training/Terios')
    os.mkdir('/tmp/datasets/training/Xenia')
    os.mkdir('/tmp/datasets/training/agya')
    os.mkdir('/tmp/datasets/training/all new carry pick up')
    os.mkdir('/tmp/datasets/training/almaz')
    os.mkdir('/tmp/datasets/training/alphard')
    os.mkdir('/tmp/datasets/training/apv arena')
    os.mkdir('/tmp/datasets/training/avanza')
    os.mkdir('/tmp/datasets/training/ayla')
    os.mkdir('/tmp/datasets/training/baleno')
    os.mkdir('/tmp/datasets/training/calya')
    os.mkdir('/tmp/datasets/training/camry')
    os.mkdir('/tmp/datasets/training/camry hybrid')
    os.mkdir('/tmp/datasets/training/confero')
    os.mkdir('/tmp/datasets/training/corolla altis')
    os.mkdir('/tmp/datasets/training/corolla altis hybrid')
    os.mkdir('/tmp/datasets/training/corolla cross')
    os.mkdir('/tmp/datasets/training/cortez')
    os.mkdir('/tmp/datasets/training/ertiga')
    os.mkdir('/tmp/datasets/training/formo')
    os.mkdir('/tmp/datasets/training/fortuner')
    os.mkdir('/tmp/datasets/training/gran max mb')
    os.mkdir('/tmp/datasets/training/gran max pickup')
    os.mkdir('/tmp/datasets/training/hilux d cab')
    os.mkdir('/tmp/datasets/training/hilux s cab')
    os.mkdir('/tmp/datasets/training/ignis')
    os.mkdir('/tmp/datasets/training/jimny')
    os.mkdir('/tmp/datasets/training/kijang innova')
    os.mkdir('/tmp/datasets/training/land cruiser')
    os.mkdir('/tmp/datasets/training/luxio')
    os.mkdir('/tmp/datasets/training/rocky')
    os.mkdir('/tmp/datasets/training/rush')
    os.mkdir('/tmp/datasets/training/sienta')
    os.mkdir('/tmp/datasets/training/sigra')
    os.mkdir('/tmp/datasets/training/sirion')
    os.mkdir('/tmp/datasets/training/supra')
    os.mkdir('/tmp/datasets/training/vellfire')
    os.mkdir('/tmp/datasets/training/veloz')
    os.mkdir('/tmp/datasets/training/venturer')
    os.mkdir('/tmp/datasets/training/vios')
    os.mkdir('/tmp/datasets/training/voxy')
    os.mkdir('/tmp/datasets/training/yaris')
    os.mkdir('/tmp/datasets/testing/86')
    os.mkdir('/tmp/datasets/testing/C-HR Hybrid')
    os.mkdir('/tmp/datasets/testing/C-Hr')
    os.mkdir('/tmp/datasets/testing/Hi-Max')
    os.mkdir('/tmp/datasets/testing/HiAce')
    os.mkdir('/tmp/datasets/testing/Karimun Wagon R')
    os.mkdir('/tmp/datasets/testing/Raize')
    os.mkdir('/tmp/datasets/testing/Terios')
    os.mkdir('/tmp/datasets/testing/Xenia')
    os.mkdir('/tmp/datasets/testing/agya')
    os.mkdir('/tmp/datasets/testing/all new carry pick up')
    os.mkdir('/tmp/datasets/testing/almaz')
    os.mkdir('/tmp/datasets/testing/alphard')
    os.mkdir('/tmp/datasets/testing/apv arena')
    os.mkdir('/tmp/datasets/testing/avanza')
    os.mkdir('/tmp/datasets/testing/ayla')
    os.mkdir('/tmp/datasets/testing/baleno')
    os.mkdir('/tmp/datasets/testing/calya')
    os.mkdir('/tmp/datasets/testing/camry')
    os.mkdir('/tmp/datasets/testing/camry hybrid')
    os.mkdir('/tmp/datasets/testing/confero')
    os.mkdir('/tmp/datasets/testing/corolla altis')
    os.mkdir('/tmp/datasets/testing/corolla altis hybrid')
    os.mkdir('/tmp/datasets/testing/corolla cross')
    os.mkdir('/tmp/datasets/testing/cortez')
    os.mkdir('/tmp/datasets/testing/ertiga')
    os.mkdir('/tmp/datasets/testing/formo')
    os.mkdir('/tmp/datasets/testing/fortuner')
    os.mkdir('/tmp/datasets/testing/gran max mb')
    os.mkdir('/tmp/datasets/testing/gran max pickup')
    os.mkdir('/tmp/datasets/testing/hilux d cab')
    os.mkdir('/tmp/datasets/testing/hilux s cab')
    os.mkdir('/tmp/datasets/testing/ignis')
    os.mkdir('/tmp/datasets/testing/jimny')
    os.mkdir('/tmp/datasets/testing/kijang innova')
    os.mkdir('/tmp/datasets/testing/land cruiser')
    os.mkdir('/tmp/datasets/testing/luxio')
    os.mkdir('/tmp/datasets/testing/rocky')
    os.mkdir('/tmp/datasets/testing/rush')
    os.mkdir('/tmp/datasets/testing/sienta')
    os.mkdir('/tmp/datasets/testing/sigra')
    os.mkdir('/tmp/datasets/testing/sirion')
    os.mkdir('/tmp/datasets/testing/supra')
    os.mkdir('/tmp/datasets/testing/vellfire')
    os.mkdir('/tmp/datasets/testing/veloz')
    os.mkdir('/tmp/datasets/testing/venturer')
    os.mkdir('/tmp/datasets/testing/vios')
    os.mkdir('/tmp/datasets/testing/voxy')
    os.mkdir('/tmp/datasets/testing/yaris')
except OSError:
    pass

def split_data(SOURCE, TRAINING, TESTING, SPLIT_SIZE):

  files=[]
  for filename in os.listdir(SOURCE):
    file = SOURCE + filename
    if os.path.getsize(file) > 0:
      files.append(filename)
    else:
      print('File is empty')

    training_length = int(len(files) * SPLIT_SIZE)
    testing_length = int(len(files) - training_length)
    shuffled_set = random.sample(files, len(files))
    training_set = shuffled_set[0:training_length]
    testing_set = shuffled_set[-testing_length:]
  
  for filename in training_set:
    src_file = SOURCE + filename
    dest_file = TRAINING + filename
    copyfile(src_file, dest_file)
    
  for filename in testing_set:
    src_file = SOURCE + filename
    dest_file = TESTING + filename
    copyfile(src_file, dest_file)

a86_SOURCE_DIR = "/tmp/mobil/86/"
TRAINING_86_DIR = "/tmp/datasets/training/86/"
TESTING_86_DIR = "/tmp/datasets/testing/86/"
CHRHybrid_SOURCE_DIR = "/tmp/mobil/C-HR Hybrid/"
TRAINING_CHRHybrid_DIR = "/tmp/datasets/training/C-HR Hybrid/"
TESTING_CHRHybrid_DIR = "/tmp/datasets/testing/C-HR Hybrid/"
CHR_SOURCE_DIR = "/tmp/mobil/C-Hr/"
TRAINING_CHR_DIR = "/tmp/datasets/training/C-Hr/"
TESTING_CHR_DIR = "/tmp/datasets/testing/C-Hr/"
HI_MAX_SOURCE_DIR = "/tmp/mobil/Hi-Max/"
TRAINING_HI_MAX_DIR = "/tmp/datasets/training/Hi-Max/"
TESTING_HI_MAX_DIR = "/tmp/datasets/testing/Hi-Max/"
HiAce_SOURCE_DIR = "/tmp/mobil/HiAce/"
TRAINING_HiAce_DIR = "/tmp/datasets/training/HiAce/"
TESTING_HiAce_DIR = "/tmp/datasets/testing/HiAce/"
Karimun_Wagon_R_SOURCE_DIR = "/tmp/mobil/Karimun Wagon R/"
TRAINING_Karimun_Wagon_R_DIR = "/tmp/datasets/training/Karimun Wagon R/"
TESTING_Karimun_Wagon_R_DIR = "/tmp/datasets/testing/Karimun Wagon R/"
Raize_SOURCE_DIR = "/tmp/mobil/Raize/"
TRAINING_Raize_DIR = "/tmp/datasets/training/Raize/"
TESTING_Raize_DIR = "/tmp/datasets/testing/Raize/"
Terios_SOURCE_DIR = "/tmp/mobil/Terios/"
TRAINING_Terios_DIR = "/tmp/datasets/training/Terios/"
TESTING_Terios_DIR = "/tmp/datasets/testing/Terios/"
Xenia_SOURCE_DIR = "/tmp/mobil/Xenia/"
TRAINING_Xenia_DIR = "/tmp/datasets/training/Xenia/"
TESTING_Xenia_DIR = "/tmp/datasets/testing/Xenia/"
agya_SOURCE_DIR = "/tmp/mobil/agya/"
TRAINING_agya_DIR = "/tmp/datasets/training/agya/"
TESTING_agya_DIR = "/tmp/datasets/testing/agya/"
all_new_carry_pick_up_SOURCE_DIR = "/tmp/mobil/all new carry pick up/"
TRAINING_all_new_carry_pick_up_DIR = "/tmp/datasets/training/all new carry pick up/"
TESTING_all_new_carry_pick_up_DIR = "/tmp/datasets/testing/all new carry pick up/"
almaz_SOURCE_DIR = "/tmp/mobil/almaz/"
TRAINING_almaz_DIR = "/tmp/datasets/training/almaz/"
TESTING_almaz_DIR = "/tmp/datasets/testing/almaz/"
alphard_SOURCE_DIR = "/tmp/mobil/alphard/"
TRAINING_alphard_DIR = "/tmp/datasets/training/alphard/"
TESTING_alphard_DIR = "/tmp/datasets/testing/alphard/"
apv_arena_SOURCE_DIR = "/tmp/mobil/apv arena/"
TRAINING_apv_arena_DIR = "/tmp/datasets/training/apv arena/"
TESTING_apv_arena_DIR = "/tmp/datasets/testing/apv arena/"
avanza_SOURCE_DIR = "/tmp/mobil/avanza/"
TRAINING_avanza_DIR = "/tmp/datasets/training/avanza/"
TESTING_avanza_DIR = "/tmp/datasets/testing/avanza/"
ayla_SOURCE_DIR = "/tmp/mobil/ayla/"
TRAINING_ayla_DIR = "/tmp/datasets/training/ayla/"
TESTING_ayla_DIR = "/tmp/datasets/testing/ayla/"
baleno_SOURCE_DIR = "/tmp/mobil/baleno/"
TRAINING_baleno_DIR = "/tmp/datasets/training/baleno/"
TESTING_baleno_DIR = "/tmp/datasets/testing/baleno/"
calya_SOURCE_DIR = "/tmp/mobil/calya/"
TRAINING_calya_DIR = "/tmp/datasets/training/calya/"
TESTING_calya_DIR = "/tmp/datasets/testing/calya/"
camry_SOURCE_DIR = "/tmp/mobil/camry/"
TRAINING_camry_DIR = "/tmp/datasets/training/camry/"
TESTING_camry_DIR = "/tmp/datasets/testing/camry/"
camry_hybrid_SOURCE_DIR = "/tmp/mobil/camry hybrid/"
TRAINING_camry_hybrid_DIR = "/tmp/datasets/training/camry hybrid/"
TESTING_camry_hybrid_DIR = "/tmp/datasets/testing/camry hybrid/"
confero_SOURCE_DIR = "/tmp/mobil/confero/"
TRAINING_confero_DIR = "/tmp/datasets/training/confero/"
TESTING_confero_DIR = "/tmp/datasets/testing/confero/"
corolla_altis_SOURCE_DIR = "/tmp/mobil/corolla altis/"
TRAINING_corolla_altis_DIR = "/tmp/datasets/training/corolla altis/"
TESTING_corolla_altis_DIR = "/tmp/datasets/testing/corolla altis/"
corolla_altis_hybrid_SOURCE_DIR = "/tmp/mobil/corolla altis hybrid/"
TRAINING_corolla_altis_hybrid_DIR = "/tmp/datasets/training/corolla altis hybrid/"
TESTING_corolla_altis_hybrid_DIR = "/tmp/datasets/testing/corolla altis hybrid/"
corolla_cross_SOURCE_DIR = "/tmp/mobil/corolla cross/"
TRAINING_corolla_cross_DIR = "/tmp/datasets/training/corolla cross/"
TESTING_corolla_cross_DIR = "/tmp/datasets/testing/corolla cross/"
cortez_SOURCE_DIR = "/tmp/mobil/cortez/"
TRAINING_cortez_DIR = "/tmp/datasets/training/cortez/"
TESTING_cortez_DIR = "/tmp/datasets/testing/cortez/"
ertiga_SOURCE_DIR = "/tmp/mobil/ertiga/"
TRAINING_ertiga_DIR = "/tmp/datasets/training/ertiga/"
TESTING_ertiga_DIR = "/tmp/datasets/testing/ertiga/"
formo_SOURCE_DIR = "/tmp/mobil/formo/"
TRAINING_formo_DIR = "/tmp/datasets/training/formo/"
TESTING_formo_DIR = "/tmp/datasets/testing/formo/"
fortuner_SOURCE_DIR = "/tmp/mobil/fortuner/"
TRAINING_fortuner_DIR = "/tmp/datasets/training/fortuner/"
TESTING_fortuner_DIR = "/tmp/datasets/testing/fortuner/"
gran_max_mb_SOURCE_DIR = "/tmp/mobil/gran max mb/"
TRAINING_gran_max_mb_DIR = "/tmp/datasets/training/gran max mb/"
TESTING_gran_max_mb_DIR = "/tmp/datasets/testing/gran max mb/"
gran_max_pickup_SOURCE_DIR = "/tmp/mobil/gran max pickup/"
TRAINING_gran_max_pickup_DIR = "/tmp/datasets/training/gran max pickup/"
TESTING_gran_max_pickup_DIR = "/tmp/datasets/testing/gran max pickup/"
hilux_d_cab_SOURCE_DIR = "/tmp/mobil/hilux d cab/"
TRAINING_hilux_d_cab_DIR = "/tmp/datasets/training/hilux d cab/"
TESTING_hilux_d_cab_DIR = "/tmp/datasets/testing/hilux d cab/"
hilux_s_cab_SOURCE_DIR = "/tmp/mobil/hilux s cab/"
TRAINING_hilux_s_cab_DIR = "/tmp/datasets/training/hilux s cab/"
TESTING_hilux_s_cab_DIR = "/tmp/datasets/testing/hilux s cab/"
ignis_SOURCE_DIR = "/tmp/mobil/ignis/"
TRAINING_ignis_DIR = "/tmp/datasets/training/ignis/"
TESTING_ignis_DIR = "/tmp/datasets/testing/ignis/"
jimny_SOURCE_DIR = "/tmp/mobil/jimny/"
TRAINING_jimny_DIR = "/tmp/datasets/training/jimny/"
TESTING_jimny_DIR = "/tmp/datasets/testing/jimny/"
kijang_innova_SOURCE_DIR = "/tmp/mobil/kijang innova/"
TRAINING_kijang_innova_DIR = "/tmp/datasets/training/kijang innova/"
TESTING_kijang_innova_DIR = "/tmp/datasets/testing/kijang innova/"
land_cruiser_SOURCE_DIR = "/tmp/mobil/land cruiser/"
TRAINING_land_cruiser_DIR = "/tmp/datasets/training/land cruiser/"
TESTING_land_cruiser_DIR = "/tmp/datasets/testing/land cruiser/"
luxio_SOURCE_DIR = "/tmp/mobil/luxio/"
TRAINING_luxio_DIR = "/tmp/datasets/training/luxio/"
TESTING_luxio_DIR = "/tmp/datasets/testing/luxio/"
rocky_SOURCE_DIR = "/tmp/mobil/rocky/"
TRAINING_rocky_DIR = "/tmp/datasets/training/rocky/"
TESTING_rocky_DIR = "/tmp/datasets/testing/rocky/"
rush_SOURCE_DIR = "/tmp/mobil/rush/"
TRAINING_rush_DIR = "/tmp/datasets/training/rush/"
TESTING_rush_DIR = "/tmp/datasets/testing/rush/"
sienta_SOURCE_DIR = "/tmp/mobil/sienta/"
TRAINING_sienta_DIR = "/tmp/datasets/training/sienta/"
TESTING_sienta_DIR = "/tmp/datasets/testing/sienta/"
sigra_SOURCE_DIR = "/tmp/mobil/sigra/"
TRAINING_sigra_DIR = "/tmp/datasets/training/sigra/"
TESTING_sigra_DIR = "/tmp/datasets/testing/sigra/"
sirion_SOURCE_DIR = "/tmp/mobil/sirion/"
TRAINING_sirion_DIR = "/tmp/datasets/training/sirion/"
TESTING_sirion_DIR = "/tmp/datasets/testing/sirion/"
supra_SOURCE_DIR = "/tmp/mobil/supra/"
TRAINING_supra_DIR = "/tmp/datasets/training/supra/"
TESTING_supra_DIR = "/tmp/datasets/testing/supra/"
vellfire_SOURCE_DIR = "/tmp/mobil/vellfire/"
TRAINING_vellfire_DIR = "/tmp/datasets/training/vellfire/"
TESTING_vellfire_DIR = "/tmp/datasets/testing/vellfire/"
veloz_SOURCE_DIR = "/tmp/mobil/veloz/"
TRAINING_veloz_DIR = "/tmp/datasets/training/veloz/"
TESTING_veloz_DIR = "/tmp/datasets/testing/veloz/"
venturer_SOURCE_DIR = "/tmp/mobil/venturer/"
TRAINING_venturer_DIR = "/tmp/datasets/training/venturer/"
TESTING_venturer_DIR = "/tmp/datasets/testing/venturer/"
vios_SOURCE_DIR = "/tmp/mobil/vios/"
TRAINING_vios_DIR = "/tmp/datasets/training/vios/"
TESTING_vios_DIR = "/tmp/datasets/testing/vios/"
voxy_SOURCE_DIR = "/tmp/mobil/voxy/"
TRAINING_voxy_DIR = "/tmp/datasets/training/voxy/"
TESTING_voxy_DIR = "/tmp/datasets/testing/voxy/"
yaris_SOURCE_DIR = "/tmp/mobil/yaris/"
TRAINING_yaris_DIR = "/tmp/datasets/training/yaris/"
TESTING_yaris_DIR = "/tmp/datasets/testing/yaris/"

split_size = .8
split_data(a86_SOURCE_DIR, TRAINING_86_DIR, TESTING_86_DIR, split_size)
split_data(CHRHybrid_SOURCE_DIR, TRAINING_CHRHybrid_DIR, TESTING_CHRHybrid_DIR, split_size)
split_data(CHR_SOURCE_DIR, TRAINING_CHR_DIR, TESTING_CHR_DIR, split_size)
split_data(HI_MAX_SOURCE_DIR, TRAINING_HI_MAX_DIR, TESTING_HI_MAX_DIR, split_size)
split_data(HiAce_SOURCE_DIR, TRAINING_HiAce_DIR, TESTING_HiAce_DIR, split_size)
split_data(Karimun_Wagon_R_SOURCE_DIR, TRAINING_Karimun_Wagon_R_DIR, TESTING_Karimun_Wagon_R_DIR, split_size)
split_data(Raize_SOURCE_DIR, TRAINING_Raize_DIR, TESTING_Raize_DIR, split_size)
split_data(Terios_SOURCE_DIR, TRAINING_Terios_DIR, TESTING_Terios_DIR, split_size)
split_data(Xenia_SOURCE_DIR, TRAINING_Xenia_DIR, TESTING_Xenia_DIR, split_size)
split_data(agya_SOURCE_DIR, TRAINING_agya_DIR, TESTING_agya_DIR, split_size)
split_data(all_new_carry_pick_up_SOURCE_DIR, TRAINING_all_new_carry_pick_up_DIR, TESTING_all_new_carry_pick_up_DIR, split_size)
split_data(almaz_SOURCE_DIR, TRAINING_almaz_DIR, TESTING_almaz_DIR, split_size)
split_data(alphard_SOURCE_DIR, TRAINING_alphard_DIR, TESTING_alphard_DIR, split_size)
split_data(apv_arena_SOURCE_DIR, TRAINING_apv_arena_DIR, TESTING_apv_arena_DIR, split_size)
split_data(avanza_SOURCE_DIR, TRAINING_avanza_DIR, TESTING_avanza_DIR, split_size)
split_data(ayla_SOURCE_DIR, TRAINING_ayla_DIR, TESTING_ayla_DIR, split_size)
split_data(baleno_SOURCE_DIR, TRAINING_baleno_DIR, TESTING_baleno_DIR, split_size)
split_data(calya_SOURCE_DIR, TRAINING_calya_DIR, TESTING_calya_DIR, split_size)
split_data(camry_SOURCE_DIR, TRAINING_camry_DIR, TESTING_camry_DIR, split_size)
split_data(camry_hybrid_SOURCE_DIR, TRAINING_camry_hybrid_DIR, TESTING_camry_hybrid_DIR, split_size)
split_data(confero_SOURCE_DIR, TRAINING_confero_DIR, TESTING_confero_DIR, split_size)
split_data(corolla_altis_SOURCE_DIR, TRAINING_corolla_altis_DIR, TESTING_corolla_altis_DIR, split_size)
split_data(corolla_altis_hybrid_SOURCE_DIR, TRAINING_corolla_altis_hybrid_DIR, TESTING_corolla_altis_hybrid_DIR, split_size)
split_data(corolla_cross_SOURCE_DIR, TRAINING_corolla_cross_DIR, TESTING_corolla_cross_DIR, split_size)
split_data(cortez_SOURCE_DIR, TRAINING_cortez_DIR, TESTING_cortez_DIR, split_size)
split_data(ertiga_SOURCE_DIR, TRAINING_ertiga_DIR, TESTING_ertiga_DIR, split_size)
split_data(formo_SOURCE_DIR, TRAINING_formo_DIR, TESTING_formo_DIR, split_size)
split_data(fortuner_SOURCE_DIR, TRAINING_fortuner_DIR, TESTING_fortuner_DIR, split_size)
split_data(gran_max_mb_SOURCE_DIR, TRAINING_gran_max_mb_DIR, TESTING_gran_max_mb_DIR, split_size)
split_data(gran_max_pickup_SOURCE_DIR, TRAINING_gran_max_pickup_DIR, TESTING_gran_max_pickup_DIR, split_size)
split_data(hilux_d_cab_SOURCE_DIR, TRAINING_hilux_d_cab_DIR, TESTING_hilux_d_cab_DIR, split_size)
split_data(hilux_s_cab_SOURCE_DIR, TRAINING_hilux_s_cab_DIR, TESTING_hilux_s_cab_DIR, split_size)
split_data(ignis_SOURCE_DIR, TRAINING_ignis_DIR, TESTING_ignis_DIR, split_size)
split_data(jimny_SOURCE_DIR, TRAINING_jimny_DIR, TESTING_jimny_DIR, split_size)
split_data(kijang_innova_SOURCE_DIR, TRAINING_kijang_innova_DIR, TESTING_kijang_innova_DIR, split_size)
split_data(land_cruiser_SOURCE_DIR, TRAINING_land_cruiser_DIR, TESTING_land_cruiser_DIR, split_size)
split_data(luxio_SOURCE_DIR, TRAINING_luxio_DIR, TESTING_luxio_DIR, split_size)
split_data(rocky_SOURCE_DIR, TRAINING_rocky_DIR, TESTING_rocky_DIR, split_size)
split_data(rush_SOURCE_DIR, TRAINING_rush_DIR, TESTING_rush_DIR, split_size)
split_data(sienta_SOURCE_DIR, TRAINING_sienta_DIR, TESTING_sienta_DIR, split_size)
split_data(sigra_SOURCE_DIR, TRAINING_sigra_DIR, TESTING_sigra_DIR, split_size)
split_data(sirion_SOURCE_DIR, TRAINING_sirion_DIR, TESTING_sirion_DIR, split_size)
split_data(supra_SOURCE_DIR, TRAINING_supra_DIR, TESTING_supra_DIR, split_size)
split_data(vellfire_SOURCE_DIR, TRAINING_vellfire_DIR, TESTING_vellfire_DIR, split_size)
split_data(veloz_SOURCE_DIR, TRAINING_veloz_DIR, TESTING_veloz_DIR, split_size)
split_data(venturer_SOURCE_DIR, TRAINING_venturer_DIR, TESTING_venturer_DIR, split_size)
split_data(vios_SOURCE_DIR, TRAINING_vios_DIR, TESTING_vios_DIR, split_size)
split_data(voxy_SOURCE_DIR, TRAINING_voxy_DIR, TESTING_voxy_DIR, split_size)
split_data(yaris_SOURCE_DIR, TRAINING_yaris_DIR, TESTING_yaris_DIR, split_size)

print(len(os.listdir('/tmp/datasets/training/86')))
print(len(os.listdir('/tmp/datasets/training/C-HR Hybrid')))
print(len(os.listdir('/tmp/datasets/training/C-Hr')))
print(len(os.listdir('/tmp/datasets/training/Hi-Max')))
print(len(os.listdir('/tmp/datasets/training/HiAce')))
print(len(os.listdir('/tmp/datasets/training/Karimun Wagon R')))
print(len(os.listdir('/tmp/datasets/training/Raize')))
print(len(os.listdir('/tmp/datasets/training/Terios')))
print(len(os.listdir('/tmp/datasets/training/Xenia')))
print(len(os.listdir('/tmp/datasets/training/agya')))
print(len(os.listdir('/tmp/datasets/training/all new carry pick up')))
print(len(os.listdir('/tmp/datasets/training/almaz')))
print(len(os.listdir('/tmp/datasets/training/alphard')))
print(len(os.listdir('/tmp/datasets/training/apv arena')))
print(len(os.listdir('/tmp/datasets/training/avanza')))
print(len(os.listdir('/tmp/datasets/training/ayla')))
print(len(os.listdir('/tmp/datasets/training/baleno')))
print(len(os.listdir('/tmp/datasets/training/calya')))
print(len(os.listdir('/tmp/datasets/training/camry')))
print(len(os.listdir('/tmp/datasets/training/camry hybrid')))
print(len(os.listdir('/tmp/datasets/training/confero')))
print(len(os.listdir('/tmp/datasets/training/corolla altis')))
print(len(os.listdir('/tmp/datasets/training/corolla altis hybrid')))
print(len(os.listdir('/tmp/datasets/training/corolla cross')))
print(len(os.listdir('/tmp/datasets/training/cortez')))
print(len(os.listdir('/tmp/datasets/training/ertiga')))
print(len(os.listdir('/tmp/datasets/training/formo')))
print(len(os.listdir('/tmp/datasets/training/fortuner')))
print(len(os.listdir('/tmp/datasets/training/gran max mb')))
print(len(os.listdir('/tmp/datasets/training/gran max pickup')))
print(len(os.listdir('/tmp/datasets/training/hilux d cab')))
print(len(os.listdir('/tmp/datasets/training/hilux s cab')))
print(len(os.listdir('/tmp/datasets/training/ignis')))
print(len(os.listdir('/tmp/datasets/training/jimny')))
print(len(os.listdir('/tmp/datasets/training/kijang innova')))
print(len(os.listdir('/tmp/datasets/training/land cruiser')))
print(len(os.listdir('/tmp/datasets/training/luxio')))
print(len(os.listdir('/tmp/datasets/training/rocky')))
print(len(os.listdir('/tmp/datasets/training/rush')))
print(len(os.listdir('/tmp/datasets/training/sienta')))
print(len(os.listdir('/tmp/datasets/training/sigra')))
print(len(os.listdir('/tmp/datasets/training/sirion')))
print(len(os.listdir('/tmp/datasets/training/supra')))
print(len(os.listdir('/tmp/datasets/training/vellfire')))
print(len(os.listdir('/tmp/datasets/training/veloz')))
print(len(os.listdir('/tmp/datasets/training/venturer')))
print(len(os.listdir('/tmp/datasets/training/vios')))
print(len(os.listdir('/tmp/datasets/training/voxy')))
print(len(os.listdir('/tmp/datasets/training/yaris')))

print(len(os.listdir('/tmp/datasets/testing/86')))
print(len(os.listdir('/tmp/datasets/testing/C-HR Hybrid')))
print(len(os.listdir('/tmp/datasets/testing/C-Hr')))
print(len(os.listdir('/tmp/datasets/testing/Hi-Max')))
print(len(os.listdir('/tmp/datasets/testing/HiAce')))
print(len(os.listdir('/tmp/datasets/testing/Karimun Wagon R')))
print(len(os.listdir('/tmp/datasets/testing/Raize')))
print(len(os.listdir('/tmp/datasets/testing/Terios')))
print(len(os.listdir('/tmp/datasets/testing/Xenia')))
print(len(os.listdir('/tmp/datasets/testing/agya')))
print(len(os.listdir('/tmp/datasets/testing/all new carry pick up')))
print(len(os.listdir('/tmp/datasets/testing/almaz')))
print(len(os.listdir('/tmp/datasets/testing/alphard')))
print(len(os.listdir('/tmp/datasets/testing/apv arena')))
print(len(os.listdir('/tmp/datasets/testing/avanza')))
print(len(os.listdir('/tmp/datasets/testing/ayla')))
print(len(os.listdir('/tmp/datasets/testing/baleno')))
print(len(os.listdir('/tmp/datasets/testing/calya')))
print(len(os.listdir('/tmp/datasets/testing/camry')))
print(len(os.listdir('/tmp/datasets/testing/camry hybrid')))
print(len(os.listdir('/tmp/datasets/testing/confero')))
print(len(os.listdir('/tmp/datasets/testing/corolla altis')))
print(len(os.listdir('/tmp/datasets/testing/corolla altis hybrid')))
print(len(os.listdir('/tmp/datasets/testing/corolla cross')))
print(len(os.listdir('/tmp/datasets/testing/cortez')))
print(len(os.listdir('/tmp/datasets/testing/ertiga')))
print(len(os.listdir('/tmp/datasets/testing/formo')))
print(len(os.listdir('/tmp/datasets/testing/fortuner')))
print(len(os.listdir('/tmp/datasets/testing/gran max mb')))
print(len(os.listdir('/tmp/datasets/testing/gran max pickup')))
print(len(os.listdir('/tmp/datasets/testing/hilux d cab')))
print(len(os.listdir('/tmp/datasets/testing/hilux s cab')))
print(len(os.listdir('/tmp/datasets/testing/ignis')))
print(len(os.listdir('/tmp/datasets/testing/jimny')))
print(len(os.listdir('/tmp/datasets/testing/kijang innova')))
print(len(os.listdir('/tmp/datasets/testing/land cruiser')))
print(len(os.listdir('/tmp/datasets/testing/luxio')))
print(len(os.listdir('/tmp/datasets/testing/rocky')))
print(len(os.listdir('/tmp/datasets/testing/rush')))
print(len(os.listdir('/tmp/datasets/testing/sienta')))
print(len(os.listdir('/tmp/datasets/testing/sigra')))
print(len(os.listdir('/tmp/datasets/testing/sirion')))
print(len(os.listdir('/tmp/datasets/testing/supra')))
print(len(os.listdir('/tmp/datasets/testing/vellfire')))
print(len(os.listdir('/tmp/datasets/testing/veloz')))
print(len(os.listdir('/tmp/datasets/testing/venturer')))
print(len(os.listdir('/tmp/datasets/testing/vios')))
print(len(os.listdir('/tmp/datasets/testing/voxy')))
print(len(os.listdir('/tmp/datasets/testing/yaris')))

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16,(3,3), activation = 'relu', input_shape=(150,150,3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(32,(3,3), activation = 'relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64,(3,3), activation = 'relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation = 'relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer=RMSprop(learning_rate=0.001), loss='binary_crossentropy', metrics=['acc'])

TRAINING_DIR = '/tmp/datasets/training'
train_datagen = ImageDataGenerator(rescale=1.0/255.)
train_generator = train_datagen.flow_from_directory(TRAINING_DIR,
                                                         batch_size=100,
                                                         class_mode='categorical', 
                                                         target_size=(150,150))

VALIDATION_DIR = '/tmp/datasets/testing'
validation_datagen = ImageDataGenerator(rescale=1.0/255.)
validation_generator = validation_datagen.flow_from_directory(VALIDATION_DIR,
                                                         batch_size=100,
                                                         class_mode='categorical', 
                                                         target_size=(150,150))

history = model.fit(train_generator,
                              epochs=20,
                              verbose=1,
                              validation_data=validation_generator)

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

import matplotlib.image  as mpimg
import matplotlib.pyplot as plt

acc=history.history['acc']
val_acc=history.history['val_acc']
loss=history.history['loss']
val_loss=history.history['val_loss']

epochs=range(len(acc)) 
plt.plot(epochs, acc, 'r', "Training Accuracy")
plt.plot(epochs, val_acc, 'b', "Validation Accuracy")
plt.title('Training and validation accuracy')
plt.figure()

plt.plot(epochs, loss, 'r', "Training Loss")
plt.plot(epochs, val_loss, 'b', "Validation Loss")


plt.title('Training and validation loss')

import numpy as np
from google.colab import files
from keras.preprocessing import image
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import img_to_array, load_img

mobilconfirm=str(input("Mobil anda adalah :"))
uploaded = files.upload()

for fn in uploaded.keys():
 
  # predicting images
  path = '/content/' + fn
  img = image.load_img(path, target_size=(150,150))
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  
  plt.imshow(load_img(fn))
  plt.show()
  images = np.vstack([x])
  classes = model.predict(images, batch_size=10)
  print(classes[0])
  if classes[0]<0.02 and mobilconfirm=="86":
    print(fn + " Benar 86")
  elif 0.02<classes[0]<0.04 and mobilconfirm=="C-HR Hybrid":
    print(fn + " Benar C-HR Hybrid")  
  elif 0.04<classes[0]<0.06 and mobilconfirm=="C-Hr":
    print(fn + " Benar C-Hr")
  elif 0.08<classes[0]<0.1 and mobilconfirm=="Hi-Max":
    print(fn + " Benar Hi-Max") 
  elif 0.1<classes[0]<0.12 and mobilconfirm=="HiAce":
    print(fn + " Benar HiAce")   
  elif 0.12<classes[0]<0.14 and mobilconfirm=="Karimun Wagon R":
    print(fn + " Benar Karimun Wagon R")    
  else:
    print("data blm masuk")