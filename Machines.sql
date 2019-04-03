--
-- Create table for each machine
-- M052 is in M1998
-- M06 is in M2002
--

DROP TABLE IF EXISTS M1998;
DROP TABLE IF EXISTS M2002;
DROP TABLE IF EXISTS M04;

CREATE TABLE M1998 (
M1998_ID INT NOT NULL AUTO_INCREMENT,
K0100_54 VARCHAR(50),
K1001_950273 VARCHAR(50),
K1002_ReNi_HJD VARCHAR(50),
K1004_30.10.2018_11:07:55 VARCHAR(50),
K1053_20181030
K1081_M1998
K1082_GEM_Suzhou
K1086
K1100_steering
K1103
K1104_30.10.2018_09:45:00
K1222_MFL
K1303_TK-PCHZ
K2001/1_1
K2002/1_C_052_SM_pos_bef_join_TD1_actual
K2004/1_0
K2022/1_3
K2101/1_1.139
K2112/1_-0.01
K2113/1_0.01
K2142/1_mm
K2001/2_2
K2002/2_C_052_SM_pos_bef_join_TD1_difference
K2004/2_0
K2022/2_3
K2101/2_0
K2112/2_-0.01
K2113/2_0.01
K2142/2_mm
K2001/3_3
K2002/3_C_052_SM_pos_bef_join_TD2_actual
K2004/3_0
K2022/3_3
K2101/3_1.139
K2112/3_-0.01
K2113/3_0.01
K2142/3_mm
K2001/4_4
K2002/4_C_052_SM_pos_bef_join_TD2_difference
K2004/4_0
K2022/4_3
K2101/4_0
K2112/4_-0.01
K2113/4_0.01
K2142/4_mm
K2001/5_5
K2002/5_C_052_SM_join_stator_actual
K2004/5_0
K2022/5_3
K2101/5_152.019
K2112/5_-0.02
K2113/5_0.2
K2142/5_mm
K2001/6_6
K2002/6_C_052_SM_join_stator_difference
K2004/6_0
K2022/6_3
K2101/6_0
K2112/6_-0.02
K2113/6_0.2
K2142/6_mm
K2001/7_7
K2002/7_C_052_SM_join_magnet_actual
K2004/7_0
K2022/7_3
K2101/7_152.019
K2112/7_-0.2
K2113/7_0.2
K2142/7_mm
K2001/8_8
K2002/8_C_052_SM_Joining_magnet_difference
K2004/8_0
K2022/8_3
K2101/8_0
K2112/8_-0.2
K2113/8_0.2
K2142/8_mm
K2001/9_9
K2002/9_C_052_calibration_magnetic_field
K2004/9_0
K2022/9_3
K2112/9_-0.1
K2113/9_0.1
K2142/9_mT
K2001/10_10
K2002/10_P_052_Joining_stator_pre-position_TD1
K2004/10_0
K2022/10_3
K2101/10_81
K2112/10_-2
K2113/10_2
K2142/10_mm
K2001/11_11
K2002/11_P_052_Joining_Stator_-_measuring_pre-position_TD2
K2004/11_0
K2022/11_3
K2101/11_81
K2112/11_-2
K2113/11_2
K2142/11_mm
K2001/12_12
K2002/12_Q_052_Joining_stator_delta_measuring_pre-position
K2004/12_0
K2022/12_3
K2110/12_-0.1
K2111/12_0.3
K2142/12_mm
K2001/13_13
K2002/13_Q_052_Joining_stator_measuring_pre-position_average
K2004/13_0
K2022/13_3
K2101/13_81
K2112/13_-2
K2113/13_2
K2142/13_mm
K2001/14_14
K2002/14_P_052_Joining_stator_-_measuring_position_after_joining_TD1
K2004/14_0
K2022/14_3
K2101/14_81
K2112/14_-2
K2113/14_2
K2142/14_mm
K2001/15_15
K2002/15_P_052_Joining_stator_-_measuring_position_after_joining_TD2
K2004/15_0
K2022/15_3
K2101/15_81
K2112/15_-2
K2113/15_2
K2142/15_mm
K2001/16_16
K2002/16_P_052_Joining_stator_-_Force-max_Zone_0
K2004/16_0
K2110/16_-50
K2111/16_2500
K2142/16_N
K2001/17_17
K2002/17_P_052_Joining_stator_-_Force-max_Zone_1
K2004/17_0
K2110/17_400
K2111/17_5555
K2142/17_N
K2001/18_18
K2002/18_Q_052_Joining_stator_-_Force-min_Zone_1
K2004/18_0
K2110/18_400
K2111/18_5555
K2142/18_N
K2001/19_19
K2002/19_P_052_Joining_stator_-_Force-Average_value_Zone_1
K2004/19 0
K2110/19 400
K2111/19 5555
K2142/19 N
K2001/20 20
K2002/20 Q_052 Joining stator - Force-max Zone 2
K2004/20 0
K2110/20 1200
K2111/20 5000
K2142/20 N
K2001/21 21
K2002/21 Q_052 Joining stator - Force-min Zone 2
K2004/21 0
K2110/21 1200
K2111/21 5000
K2142/21 N
K2001/22 22
K2002/22 P_052 Joining stator - Force-Average value Zone 2
K2004/22 0
K2110/22 1200
K2111/22 5000
K2142/22 N
K2001/23 23
K2002/23 P_052 Joining stator - Delta force / End force
K2004/23 0
K2101/23 1000
K2110/23 0
K2111/23 5000
K2142/23 N
K2001/24 24
K2002/24 P_052 Joining stator - Way
K2004/24 0
K2022/24 3
K2101/24 1
K2112/24 -0.1
K2113/24 0.1
K2142/24 mm
K2001/25 25
K2002/25 P_052 Joining stator - Gradient
K2004/25 0
K2022/25 3
K2101/25 0
K2110/25 0
K2111/25 0
K2142/25 N/mm
K2001/26 26
K2002/26 Q_052 Joining stator - Joining position TD1
K2004/26 0
K2022/26 3
K2142/26 mm
K2001/27 27
K2002/27 Q_052 Joining stator - Joining position TD2
K2004/27 0
K2022/27 3
K2142/27 mm
K2001/28 28
K2002/28 Q_052 Joining stator - Delta Joining position
K2004/28 0
K2022/28 3
K2110/28 -0.2
K2111/28 0.2
K2142/28 mm
K2001/29 29
K2002/29 Q_052 Joining stator - Joining position - Average
K2004/29 0
K2022/29 3
K2101/29 -1.15
K2112/29 -0.1
K2113/29 0.1
K2142/29 mm
K2001/30 30
K2002/30 Q_052 Joining stator - Joining position after Adjustment TD1
K2004/30 0
K2022/30 3
K2101/30 1.15
K2112/30 -0.1
K2113/30 0.1
K2142/30 mm
K2001/31 31
K2002/31 Q_052 Joining stator - Joining position after Adjustment TD2
K2004/31 0
K2022/31 3
K2101/31_1.15
K2112/31_-0.1
K2113/31_0.1
K2142/31_mm
K2001/32_32
K2002/32_Q_052_Joining_stator_-_Delta_Joining_position_after_Adjustment
K2004/32_0
K2022/32_3
K2110/32_-0.5
K2111/32_0.5
K2142/32_mm
K2001/33_33
K2002/33_Q_052_Joining_stator_-_Joining_position_after_Adjustment_-_Average
K2004/33_0
K2022/33_3
K2101/33_-1.15
K2112/33_-0.1
K2113/33_0.1
K2142/33_mm
K2001/34_34
K2002/34_Q_052_Joining_stator_-_Joining_position_after_Adjustment_TD_Quality
K2004/34_0
K2101/34_1.15
K2112/34_-0.1
K2113/34_0.1
K2001/35_35
K2002/35_P_052_Quality_measuring_position_stator
K2004/35_0
K2022/35_3
K2110/35_-0.5
K2111/35_0.5
K2142/35_mm
K2001/36_36
K2002/36_P_052_Joining_magnet_-_Force-Max_Zone_0
K2004/36_0
K2110/36_-30
K2111/36_4000
K2142/36_N
K2001/37_37
K2002/37_P_052_Joining_magnet_-_Force-Max_Zone_1
K2004/37_0
K2110/37_800
K2111/37_3500
K2142/37_N
K2001/38_38
K2002/38_Q_052_Joining_magnet_-_Force-Min_Zone_1
K2004/38_0
K2110/38_800
K2111/38_3500
K2142/38_N
K2001/39_39
K2002/39_P_052_Joining_magnet_-_Force-Average_value_Zone_1
K2004/39_0
K2110/39_800
K2111/39_3500
K2142/39_N
K2001/40_40
K2002/40_Q_052_Joining_magnet_-_Force-Max_Zone_2
K2004/40_0
K2110/40_1200
K2111/40_4000
K2142/40_N
K2001/41_41
K2002/41_Q_052_Joining_magnet_-_Force-Min_Zone_2
K2004/41_0
K2110/41_1200
K2111/41_4000
K2142/41_N
K2001/42_42
K2002/42_P_052_Joining_magnet_-_Force-Average_value_Zone_2
K2004/42_0
K2110/42_1200
K2111/42_4000
K2142/42_N
K2001/43_43
K2002/43_Q_052_Joining_magnet_-_Joining_position
K2004/43_0
K2022/43_3
K2101/43_90.6
K2112/43_-0.25
K2113/43_0.25
K2142/43_mm
K2001/44_44
K2002/44_P_052_Joining_magnet_-_Delta_force_/_End_force
K2004/44_0
K2101/44_800
K2110/44_0
K2111/44_5000
K2142/44_N
K2001/45_45
K2002/45_P_052_Joining_magnet_-_Way
K2004/45_0
K2022/45_3
K2101/45_0
K2112/45_0
K2113/45_0
K2142/45_mm
K2001/46_46
K2002/46_P_052_Joining_magnet_-_Gradient
K2004/46_0
K2022/46_3
K2101/46_0
K2110/46_0
K2111/46_0
K2142/46_N/mm
K2001/47_47
K2002/47_Q_052_Adjustement_orientation_tooth_spindle
K2004/47_0
K2022/47_1
K2101/47_200
K2112/47_-0,5
K2113/47_0,5
K2001/48_48
K2002/48_P_052_Adjustement_angle_MM
K2004/48_0
K2022/48_3
K2101/48_-100
K2112/48_-27
K2113/48_9
K2142/48_infinity
K2001/49_49
K2002/49_P_052_Quality_measuring_MM_after_joining_with_load
K2004/49_0
K2022/49_3
K2101/49_0
K2112/49_-1.5
K2113/49_1.5
K2142/49_mT
K2001/50_50
K2002/50_Q_052_Quality_measuring_MM_after_joining_without_load
K2004/50_0
K2022/50_3
K2101/50_0
K2112/50_-1.5
K2113/50_1.5
K2142/50_mT
K2001/51_51
K2002/51_P_052_Quality_measuring_MM_before_joining_Nest_1
K2004/51_0
K2022/51_3
K2101/51_-0.5
K2112/51_-1.2
K2113/51_1.2
K2142/51_mT
K2001/52_52
K2002/52_P_052_Quality_measuring_MM_before_joining_Nest_2
K2004/52_0
K2022/52_3
K2101/52_-0.65
K2112/52_-1.2
K2113/52_1.2
K2142/52_mT
K2001/53_53
K2002/53_P_052_Quality_measuring_MM_before_joining_Nest_3
K2004/53_0
K2022/53_3
K2101/53_-0.5
K2112/53_-1.2
K2113/53_1.2
K2142/53_mT
K2001/54_54
K2002/54_P_052_Gradient_MM
K2004/54_0
K2022/54_3
K2101/54_2
K2112/54_-2
K2113/54_15
K2142/54_mT/infinity


  M1998_name VARCHAR(50) NOT NULL,
  M1998_event VARCHAR (50) NOT NULL,
  m_country VARCHAR(15) NULL DEFAULT NULL,
  m_medal CHAR(6),
  m_time TIME NULL DEFAULT 0,
  PRIMARY KEY (m_ID),
  CONSTRAINT 
    FOREIGN KEY (m_country) REFERENCES countries (c_name),
  CONSTRAINT
	FOREIGN KEY (m_event) REFERENCES events_swimming (e_name));
	
CREATE TABLE M052 (
M052_ID INT NOT NULL AUTO_INCREMENT,
K1001 SMALLINT,
K1002 VARCHAR2(30),
K1004 VARCHAR2(30),
K1053 VARCHAR2(10),
K1081 VARCHAR2(10),
K1082 VARCHAR2(15),
K1086 VARCHAR2(10),
K1100 VARCHAR2(10),
K1103 VARCHAR2(10),
K1104 VARCHAR2(30),
K1303 VARCHAR2(10),
C_052_SM_pos_before_joining_stator_TD1_actual SMALLINT,
Attribute1 SMALLINT,
DateTime VARCHAR2(30),
Event1 SMALLINT,
Event2 SMALLINT,
Event3 SMALLINT,
Event4 SMALLINT,
Batch_number VARCHAR2(15),
Nest_number	SMALLINT,
C_052_SM_pos_before_joining_stator_TD1_difference SMALLINT,
Attribute2 SMALLINT,
C_052_SM_pos_before_joining_stator_TD2_actual SMALLINT,
Attribute3 SMALLINT,
C_052_SM_pos_before_joining_stator_TD2_difference SMALLINT,
Attribute4 SMALLINT,
C_052_SM_joining_stator_actual SMALLINT,
Attribute5 SMALLINT,
C_052_SM_joining_stator_difference SMALLINT,
Attribute6 SMALLINT,
C_052 SM_joining_magnet_actual SMALLINT,
Attribute7 SMALLINT,
C_052_SM_joining_magnet_difference SMALLINT,
Attribute8 SMALLINT,
C_052_calibration_magnetic_field SMALLINT,
Attribute9 SMALLINT,
P_052_joining_stator_measuring_pre-pos_TD1 DECIMAL(15),
Attribute10 SMALLINT,
P_052_joining_stator_measuring_pre-pos_TD2 DECIMAL(15),
Attribute11 SMALLINT,
Q_052_joining_stator_delta_measuring_pre-pos DECIMAL(15),
Attribute12 SMALLINT,
Q_052_joining_stator_measuring_pre-pos_avg DECIMAL(15),
Attribute13 SMALLINT,
P_052_joining_stator_Force-max_Zone0 SMALLINT,
Attribute14 SMALLINT,
P_052_joining_stator_Force-max_Zone1 SMALLINT,
Attribute15 SMALLINT,
Q_052_joining_stator_Force-min_Zone1 SMALLINT,
Attribute16 SMALLINT,
P_052_joining_stator_Force-avg_Zone1 SMALLINT,
Attribute17 SMALLINT,
Q_052_joining_stator_Force-max_Zone2 SMALLINT,
Attribute18 SMALLINT,
Q_052_joining_stator_Force-min_Zone2 SMALLINT,
Attribute19 SMALLINT,
P_052_joining_stator_Force-avg_Zone2 SMALLINT,
Attribute20 SMALLINT,
P_052_joining_stator_Delta_force SMALLINT,
Attribute21 SMALLINT,
P_052_joining_stator_Way SMALLINT,
Attribute22 SMALLINT,
P_052_joining_stator_Gradient SMALLINT,
Attribute23 SMALLINT,
Q_052_joining_stator_Joining_pos DECIMAL(15),
Attribute24 SMALLINT,
Q_052_joining_stator_Joining_pos_TD1 DECIMAL(15),
Attribute25 SMALLINT,
Q_052_joining_stator_Joining_pos_TD2 DECIMAL(15),
Attribute26 SMALLINT,
Q_052_joining_stator_Joining_pos_after_Adjustment_avg DECIMAL(15),
Attribute27 SMALLINT,
P_052_joining_magnet_Force-Max_Zone0 SMALLINT,
Attribute28 SMALLINT,
P_052_joining_magnet_Force-Max_Zone1 SMALLINT,
Attribute29 SMALLINT,
Q_052_joining_magnet_Force-Min_Zone1 SMALLINT,
Attribute30 SMALLINT,
P_052_joining_magnet_Force-avg_Zone1 SMALLINT,
Attribute31 SMALLINT,
Q_052_joining_magnet_Force-Max_Zone2 SMALLINT,
Attribute32 SMALLINT,
Q_052_joining_magnet_Force-Min_Zone2 SMALLINT,
Attribute33 SMALLINT,
P_052_joining_magnet_Force-avg_Zone2 SMALLINT,
Attribute34 SMALLINT,
Q_052_joining_magnet_Joining_pos DECIMAL(15),
Attribute35 SMALLINT,
P_052_joining_magnet_Delta_force SMALLINT,
Attribute36 SMALLINT,
P_052_joining_magnet_Way SMALLINT,
Attribute37 SMALLINT,
P_052_joining_magnet_Gradient SMALLINT,
Attribute38 SMALLINT,
Q_052_Adjustement_orientation_tooth_spindle SMALLINT,
Attribute39 SMALLINT,
P_052_Adjustement_angle_MM DECIMAL(15),
Attribute40 SMALLINT,
P_052_Quality_measuring_MM_after_joining_with_load DECIMAL(15),
Attribute41 SMALLINT,
Q_052_Quality_measuring_MM_after_joining_without_load DECIMAL(15),
Attribute42 SMALLINT,
P_052_Quality_measuring_MM_before_joining_Nest1 DECIMAL(15),
Attribute43 SMALLINT,
P_052_Quality_measuring_MM_before_joining_Nest2 DECIMAL(15),
Attribute44 SMALLINT,
P_052_Quality_measuring_MM_before_joining_Nest3 DECIMAL(15),
Attribute45 SMALLINT,
P_052_Gradient_MM DECIMAL(15),
Attribute46 SMALLINT,
PRIMARY KEY (M052_ID),
CONSTRAINT 
FOREIGN KEY (Batch_number) REFERENCES M06 (Batch_number));

CREATE TABLE M06 (
M06_ID INT NOT NULL AUTO_INCREMENT,
K1001 VARCHAR2(10),
K1002 VARCHAR2(10),
K1004 VARCHAR2(30),
K1053 VARCHAR2(10),
K1081 VARCHAR2(6),
K1082 VARCHAR2(40),
K1086 VARCHAR2(10),
K1100 VARCHAR2(10),
K1103 VARCHAR2(10),
K1104 VARCHAR2(30),
K1303 VARCHAR2(10),
M_06_Temperature_TSU_module DECIMAL(2),
DateTime VARCHAR2(30),
Event1 SMALLINT,
Event2 SMALLINT,
Event3 SMALLINT,
Event4 SMALLNINT,
Batch_number VARCHAR2(15),
P_06_Calibration_Cycles SMALLINT,
P_06_Endlock_endposition_positive SMALLINT,
P_06_Endlock_endtorque_positive SMALLINT,
P_06_Endlock_torque_limit_position_positive SMALLINT,
P_06_Endlock_angle_positive SMALLINT,
P_06_Endlock_endposition_negative SMALLINT,
P_06_Endlock_endtorque_negative SMALLINT,
P_06_Endlock_torque_limit_position_negative SMALLINT,
P_06_Endlock_angle_negative SMALLINT,
Q_Offset_TSU_A DECIMAL(20),
Q_Offset_TSU_B DECIMAL(20),
Q_Gain_TSU_A DECIMAL(20),
Q_Gain_TSU_B DECIMAL(20),
M_CubicFactor_TSU_A DECIMAL(20),
M_CubicFactor_TSU_B DECIMAL(20),
Q_TSU_Max_Accuracy_A_center_zone1 DECIMAL(20),
Q_TSU_Accuracy_A_offcenter_zone0 DECIMAL(20),
Q_TSU_Accuracy_A_offcenter_zone2 DECIMAL(20),
Q_TSU_Max_Hysterese_A DECIMAL(20),
Q_TSU_Max_Accuracy_B_center_zone1 DECIMAL(20),
Q_TSU_Accuracy_B_offcenter_zone0 DECIMAL(20),
Q_TSU_Accuracy_B_offcenter_zone2 DECIMAL(20),
Q_TSU_Max_Hysteresis_B DECIMAL(20),
Q_TSU_Max_Difference DECIMAL(20),
Q_TSU_Max_Symmetry_A_Zone0 DECIMAL(20),
Q_TSU_Max_Symmetry_A_Zone1 DECIMAL(20),
Q_TSU_Max_Symmetry_A_Zone2 DECIMAL(20),
Q_TSU_Max_Symmetry_B_Zone0 DECIMAL(20),
Q_TSU_Max_Symmetry_B_Zone1 DECIMAL(20),
Q_TSU_Max_Symmetry_B_Zone2 DECIMAL(20),
Q_TsuVoltage_min DECIMAL(6),
Q_TsuVoltage_max DECIMAL(6),
Q_TsuVoltage_mean DECIMAL(20),
Q_TsuCurrent_min DECIMAL(6),
Q_TsuCurrent_max DECIMAL(6),
Q_TsuCurrent_mean DECIMAL(20),
P_Gain_A_1st_run DECIMAL(20),
P_Gain_B_1st_run DECIMAL(20),
P_Offset_A_1st_run DECIMAL(20),
P_Offset_B_1st_run DECIMAL(20),
Q_Margincheck_done DECIMAL(4),
M_TsuRegister_0x10_1run_A INT,
M_TsuRegister_0x11_1run_A INT,
M_TsuRegister_0x12_1run_A INT,
M_TsuRegister_0x13_1run_A INT,
M_TsuRegister_0x14_1run_A INT,
M_TsuRegister_0x15_1run_A INT,
M_TsuRegister_0x16_1run_A INT,
M_TsuRegister_0x17_1run_A INT,
M_TsuRegister_0x18_1run_A INT,
M_TsuRegister_0x19_1run_A INT,
M_TsuRegister_0x1A_1run_A INT,
M_TsuRegister_0x10_1run_B INT,
M_TsuRegister_0x11_1run_B INT,
M_TsuRegister_0x12_1run_B INT,
M_TsuRegister_0x13_1run_B INT,
M_TsuRegister_0x14_1run_B INT,
M_TsuRegister_0x15_1run_B INT,
M_TsuRegister_0x16_1run_B INT,
M_TsuRegister_0x17_1run_B INT,
M_TsuRegister_0x18_1run_B INT,
M_TsuRegister_0x19_1run_B INT,
M_TsuRegister_0x1A_1run_B INT,
M_TsuRegister_0x10_final_A INT,
M_TsuRegister_0x11_final_A INT,
M_TsuRegister_0x12_final_A INT,
M_TsuRegister_0x13_final_A INT,
M_TsuRegister_0x14_final_A INT,
M_TsuRegister_0x15_final_A INT,
M_TsuRegister_0x16_final_A INT,
M_TsuRegister_0x17_final_A INT,
M_TsuRegister_0x18_final_A INT,
M_TsuRegister_0x19_final_A INT,
M_TsuRegister_0x1A_final_A INT,
M_TsuRegister_0x10_final_B INT,
M_TsuRegister_0x11_final_B INT,
M_TsuRegister_0x12_final_B INT,
M_TsuRegister_0x13_final_B INT,
M_TsuRegister_0x14_final_B INT,
M_TsuRegister_0x15_final_B INT,
M_TsuRegister_0x16_final_B INT,
M_TsuRegister_0x17_final_B INT,
M_TsuRegister_0x18_final_B INT,
M_TsuRegister_0x19_final_B INT,
M_TsuRegister_0x1A_final_B INT,
P_Monitoring_Offset_A DECIMAL(20),
P_Monitoring_Offset_B DECIMAL(20),
PRIMARY KEY (M06_ID),
CONSTRAINT 
FOREIGN KEY (Batch_number) REFERENCES M052 (Batch_number));