#    Copyright (C) 2019 Greenweaves Software Limited
#
#    This is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This software is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with GNU Emacs.  If not, see <http://www.gnu.org/licenses/>
#
# BA6B Compute the Number of Breakpoints in a Permutation 


from fragile import getBreakPoints

if __name__=='__main__':
   print (getBreakPoints([+1, +2, +3, +4, +5, +6, +7, +8, +9, +10, +11, +12, +13, +14, +15, +16, +17, +18, +19, +20, +21, +22, +23, +24, +25, +26, +27, +28, +29, +30, +31, +32, +33, +34, +35, +36, +37, +38, +39, +40, +41, +42, +43, +44, +45, +46, +47, +48, +49, +50, +2835, +2836, +2837, +2838, +2839, +2840, +2841, +2842, +2843, +2844, +2845, +2846, +2847, +2848, +2849, +2850, +2851, +2852, +2853, +2854, +2855, +2856, +2857, +2858, +2859, +2860, +2861, +2862, +2863, +2864, +2865, +2866, +2867, +2868, +2869, +2870, +2117, +2118, +2119, +2120, +2121, +2122, +2123, +2124, +2125, +2126, +2127, +2128, +2129, +2130, +2131, +2132, +2133, +2134, +2135, +2136, +2137, +2138, +2139, +4031, +4032, +4033, +4034, +4035, +4036, +4037, +4038, +4039, +4040, +4041, +4042, +4043, +4044, +4045, +4046, +4047, +4048, +4049, +4050, +4051, +4052, +4053, +4054, +4055, +4056, +4057, +4058, +4059, +4060, +4061, +4062, -2242, -2241, -2240, -2239, -2238, -2237, -2236, -2235, -2234, -2233, -2232, -2231, -2230, -2229, -2228, -2227, -2226, -2225, -2224, -2223, -2222, -2221, -2220, -2219, -2218, -2217, -2216, -2215, -2214, -2213, -2212, -2211, -2210, -2209, -2208, -2207, -2206, -2205, -2204, -2203, -3139, -3138, -3137, -3136, -3135, -3134, -3133, -3132, -3131, -3130, -3129, -3128, -3127, -3126, -3125, -3124, -3123, -3122, -3121, -3120, -3119, -3118, -3117, -3116, -3115, -3114, -3113, -3112, -3111, -3110, -3109, -3108, -3107, -3106, -3105, -3104, +4472, +4473, +4474, +4475, +4476, +4477, +4478, +4479, +4480, +4481, +4482, +4483, +4484, +4485, +4486, +4487, +4488, +4489, +4490, +4491, +4492, +4493, +4494, +4495, +4496, +4497, +4498, +4499, +4500, +4501, +4502, +4503, +4504, +4505, +4506, +4507, +4508, +4509, +4510, +4511, +4512, +4513, +4514, +4515, -4019, -4018, -4017, -4016, -4015, -4014, -4013, -4012, -4011, -4010, -4009, -4008, -4007, -4006, -4005, -4004, -4003, -4002, -4001, -4000, -3999, -3998, -3997, -3996, -3995, -3994, -3993, -3992, -3991, -3990, -3989, -3988, -3987, -3986, -3985, -3984, -3983, -3982, -3981, -3980, -3979, -3978, -3977, -3976, -3975, -3974, -3973, -3972, -3971, -3970, -3969, -3968, -3967, -3966, -3965, -3964, -3963, -3962, -3961, -3960, -3959, -3958, -3957, -3956, -3955, -3954, -3953, -3952, -3951, -3950, -3949, -3948, -3947, -3946, -3945, -3944, -3943, -3942, -3941, -3940, -3939, -3938, -3937, -3936, -3935, -3934, -3933, -3932, -3931, -3930, -3929, -3928, -3927, -3926, -3925, -3924, -3923, -3922, -3921, -3920, -3919, -3918, -3917, -3916, -3915, -3914, -3913, -3912, -3911, -3910, -3909, -3908, -3907, -3906, -3905, -3904, -3903, -3902, -3901, -3900, -3899, -3898, -3897, -3896, -3895, -3894, -3893, -3892, -3891, -3890, -3889, -3888, -3887, -3886, -3885, -3884, -3883, -3882, -3881, -3880, -3879, -3878, -3877, -3876, -3875, -3874, -3873, -3872, -3871, -3870, -3869, -3868, -3867, -3866, -3865, -3864, -3863, -3862, -3861, -3860, -3859, -3858, -3857, -3856, -3855, -3854, -3853, -3852, -3851, -3850, -3849, -3848, -3847, +3090, +3091, +3092, +3093, +3094, +3095, +3096, +3097, +3098, +3099, +3100, +3101, +3102, +3103, -4471, -4470, -4469, -4468, -4467, -4466, -4465, -4464, -4463, -4462, -4461, -4460, -4459, -4458, -4457, -4456, -4455, -4454, -4453, -4452, -4451, -4450, -4449, -4448, -4447, -4446, +4086, +4087, +4088, +4089, +4090, +4091, +4092, +4093, +4094, +4095, +4096, +4097, +4098, +4099, +4100, +4101, +4102, +4103, +4104, +4105, +4106, +4107, +4108, +3163, +3164, +3165, +3166, +3167, +3168, +3169, +3170, +3706, +3707, +3708, +3709, +3710, +3711, +3712, +3713, +3714, +3715, +3716, +3717, +3718, +3719, +3720, +3721, +3722, +3723, +3724, +3725, +3726, +3727, +3728, +3729, +3730, +3731, +3732, +3733, +3734, +3735, +3736, +3737, +3738, +3739, +3740, +3741, +3742, +3743, +3744, +3745, +3746, +3747, +3748, +3749, +3750, +3751, +3752, +3753, +3754, -1552, -1551, -1550, -1549, -1548, -1547, -1546, -1545, -1544, -1543, -1542, -1541, -1540, -1539, -1538, -1537, -1536, -1535, -1534, -1533, -1532, -1531, -1530, -1529, -1528, -1527, -1526, -1525, -1524, -1523, -1522, -1521, -1520, -1519, -1518, -1517, -1516, -1515, -1514, -1513, -1512, -1511, -1510, -1509, -1508, -1507, -1506, -834, -833, -832, -831, -830, -829, -828, -827, -826, -825, -824, -823, -822, -821, -820, -819, -818, -817, -816, -815, -814, -813, -812, -811, -810, -809, -808, -807, -806, -805, -804, -803, -802, -801, -800, -799, -798, -797, -796, -795, -794, -793, -792, -791, -790, -789, -788, -787, -786, -785, -784, -2176, -2175, -2174, +4146, +4147, +4148, +4149, +4150, +4151, +4152, +4153, +4154, +4155, +4156, +4157, +4158, +4159, +4160, +4161, +4162, +4163, +4164, +4165, +4166, +4167, +4168, +4169, +4170, +4171, +4172, +4173, +4174, +4175, +4176, +4177, +4178, +4179, +4180, +4181, +4182, +4183, +4184, +4185, +4186, +4187, +4188, +4189, +4190, +4191, +4192, +4193, +4194, +4195, +4196, +4197, +4198, +4199, +4200, +4201, +4202, +4203, +4204, +4205, +4206, +4207, +4208, +4209, +4210, +4211, +4212, +4213, +4214, +4215, +4216, +4217, +4218, +4219, +4220, +4221, +4222, +4223, +4224, +4225, +4226, +4227, +4228, +4229, +4230, +4231, +4232, +4233, +4234, +4235, +4236, +4237, +4238, +4239, +4240, +4241, +4242, +4243, +4244, +4245, +4246, +4247, +4248, +4249, +4250, +4251, +4252, +4253, +4254, +4255, +4256, +4257, +4258, +4259, +4260, +4261, +4262, +4263, +4264, +4265, +4266, +4267, +4268, +4269, -4391, -4390, -4389, -4388, -4387, -4386, -4385, -4384, -4383, -4382, -4381, -4380, -4379, -4378, -4377, -4376, -4375, -4374, -4373, -4372, -4371, -4370, -4369, -4368, -4367, -4366, -4365, -4364, -4363, -4362, -4361, -4360, -4359, -4358, -4357, -4356, -4355, -4354, -4353, -4352, -4351, -4350, -4349, -4348, -4347, +1334, +1335, +1336, +1337, +1338, +1339, +1340, +1341, +1342, +1343, +1344, +1345, +1346, +1347, +1348, +1349, +1350, +1351, +1352, +1353, +1354, +1355, +1356, +1357, +1358, +1359, +1360, +1361, +1362, +1363, +1364, +1365, +1366, +1367, +1368, +1369, +1370, +1371, +1372, +1373, +1374, +1375, +1376, +1377, +1378, +1379, +1380, +1381, +1382, +1383, +1384, +1385, +1386, +1387, +1388, +1389, +1390, +1391, +1392, +1393, +1394, +1395, +1396, +1397, +1398, +1399, +1400, +1401, +1402, +1403, +1404, +1405, +1406, +1407, +1408, +1409, +1410, +1411, +1412, +1413, +1414, +1415, +1416, +1417, +1418, +1419, +1420, +1421, +1422, +1423, +1424, +1425, +1426, +1427, +1428, +1429, +1430, +1431, +1432, +1433, +1434, +1435, +1436, +1437, +1438, +1439, +1440, +1441, +1442, +1443, +1444, +1445, +1446, +1447, +1448, +1449, +1450, +1451, +1452, +1453, +1454, +1455, +1456, +1457, +1458, +1459, +1460, +1461, +1462, +1463, +1464, +1465, +1466, +1467, +4026, +4027, -4430, -4429, -4428, -4427, -4426, -4425, -2989, -2988, -2987, -2986, -2985, -2984, -2983, -2982, -2981, -2980, -2979, -2978, -2977, -2976, -2975, -2974, -2973, -2972, -2971, -2970, -2969, -2968, -2967, -2966, -2965, -2964, -2963, -2962, -2961, -2960, -2959, -2958, -2957, -2956, -2955, -2954, -2953, -2952, -2951, +2396, +2397, +2398, +2399, -1825, -1824, -1823, -1822, -1821, -1820, -1819, -1818, -1817, -1816, -1815, -1814, -1813, -1812, -1811, -1810, -1809, -1808, -1807, -1806, -1805, -1804, -1803, -1802, -1801, -1800, -1799, -1798, -1797, -1796, -1795, -1794, -1793, -1792, -1791, -1790, -1789, -1788, -1787, -1786, -1785, -1784, -1783, -1782, -1781, -1780, -1779, -1778, -1777, -1776, -1775, -1774, -1773, -1772, -1771, +2559, +2560, +2561, +2562, +2563, +2564, +2565, +2566, +2567, +2568, +2569, +2570, +2571, +2572, +2573, +2574, +2575, +2576, +2577, +2578, +2579, +2580, +2581, +2582, +2583, +2584, +2585, +2586, +2587, +2588, +2589, +2590, +2591, +2592, +2593, +2594, +2595, +2596, +2597, +2598, +2599, +2600, +2601, +2602, +2603, +2604, +2605, +2606, +2607, +2608, +2609, +2610, +2611, +2612, +2613, +2614, +2615, +2616, +2617, +2618, +2619, +2620, +2621, +239, +240, +241, +242, +243, +244, +245, +246, +247, +248, +249, +250, +251, +252, +253, +254, +255, +256, +257, +258, +259, +260, +261, +262, +263, +264, +265, +266, +267, +268, +269, +270, +271, +272, +273, +274, +275, +2113, +2114, +2115, +2116, +2871, +2872, +2873, +2874, +2875, +2876, +2877, +2878, +2879, +2880, +2881, +2882, +2883, +2884, +2885, +2886, +2887, +2888, +2889, +2890, +2891, +2892, +2893, +2894, +2895, +2896, +2897, +2898, +2899, +2900, +2901, +2902, -2807, -2806, -2805, -2804, -2803, -2802, -2801, -2800, -2799, -2798, -2797, -2796, -2795, -2794, -2793, -2792, -2791, -2790, -2789, -2788, -2787, -2786, -2785, -2784, -2783, -2782, -2781, -2780, -2779, -2778, -2777, -2776, -2775, -2774, -2773, -2772, -2771, -2770, -2769, -2768, -2767, -2766, -2765, -2764, -2763, -2762, -2761, -2760, -2759, -2758, -2757, -2756, -2755, -2754, -2753, -2752, -2751, -2750, -2749, -2748, -2747, -2746, -2745, -2744, -2743, -2742, -2741, -2740, -2739, -2738, -2737, -2736, -2735, -2734, -2733, -2732, -2731, -2730, -2729, -2728, -2727, -2726, -2725, -2724, -2723, -2722, -2721, -2720, -2719, -2718, -2717, -2716, -2715, -2714, -2713, -2712, -2711, -2710, -2709, -2708, -2707, -2706, -2705, -2704, -2703, -2702, -2701, -2700, -2699, -2698, -2697, -2696, -2695, -2694, -2693, -2692, -2691, -2690, -2689, -2688, -2687, -2686, -2685, -2684, -2683, -2682, -2681, -2680, -2679, -2678, -2677, -2676, -2675, -2674, -2673, -2672, -2671, -2670, -2669, -2668, -2667, -2666, -2665, -2664, -2663, -2662, -2661, -2660, -2659, -2658, -2657, -2656, -2655, -2654, -2653, -2652, -2651, -2650, -2649, -2648, -2647, -2646, -2645, -2644, -2643, -2642, -2641, -2640, -2639, -2638, -2637, -2636, -2635, -2634, -2633, -2632, -2631, -2630, -2629, -2628, -2627, -2626, -2625, -2624, -2623, -2622, -238, -237, -236, -235, -234, -233, -232, -231, -230, -229, -228, -227, -226, -225, -224, -223, -222, -221, -220, -219, -218, -217, -216, -215, -214, -213, -212, -211, -210, -209, -208, -207, -206, -205, -204, -203, -202, -201, -200, -199, -198, -197, -196, -195, -194, -193, -192, -191, -190, -189, -188, -187, -186, -185, -184, -183, -182, -181, -180, -179, -178, -177, -176, -175, -174, -173, +142, +143, +144, +145, +146, +147, +148, +149, +150, +151, +152, +153, +154, +155, +156, +157, +158, +159, +160, +161, +162, +163, +164, +165, +166, +167, +168, +169, +170, +171, +172, -141, -140, -139, -138, -137, -136, -135, -134, -133, -132, -131, -130, -129, -128, -127, -126, -125, -124, -123, -122, -121, -120, -119, -118, -117, -116, -115, -114, -113, -112, -111, -110, +2935, +2936, +2937, +2938, +2939, +2940, +2941, +2942, +2943, +2944, +2945, +2946, +2947, +2948, +2949, +2950, +2912, +2913, +2914, +2915, +2916, +2917, +2918, +2919, +2920, +2921, +2922, +2923, +2924, +2925, +2926, -667, -666, -665, -664, -663, -662, -661, -660, -659, -658, -657, -656, -655, -654, -653, -652, -651, -650, -649, -648, -647, -646, -645, -644, -643, -642, -641, -640, -639, -638, -637, -636, -635, -634, -633, -632, -631, -630, -629, -628, -627, -626, -625, -624, -623, -622, -621, -620, -619, -618, -617, -616, -615, -614, -613, -612, -611, -610, -609, -608, -607, -606, -605, -604, -603, -602, -601, -600, -599, -598, -597, -596, -595, -594, -593, -592, -591, -590, -589, -588, -587, -586, -585, -584, -583, -582, -581, -580, -579, -578, -577, -576, -575, -574, -573, -572, -571, -570, -569, -568, -567, -566, -565, -564, -563, -562, -561, +77, +78, +79, +80, +81, +82, +83, +84, +85, +86, +87, +88, +89, +90, +91, +92, +93, +94, +95, +96, +97, +98, +99, +100, +101, +102, +103, +104, +105, +106, +107, +108, +109, -2934, -2933, -2932, -2931, -2930, -2929, -2928, -2927, +668, +669, +670, +671, +672, +673, +674, +675, +676, +677, +678, +679, +680, +681, +682, +683, +684, +685, +686, +687, +688, +689, +690, +691, +692, +693, +694, +695, +696, +697, +698, +699, +700, +701, +702, +703, +704, +705, +706, +707, +708, +709, +710, +711, +712, +713, +714, +715, +716, +717, +718, +719, +720, +721, +722, +723, +724, +725, +726, +727, +728, +729, +730, +731, +732, +733, +734, +735, +736, +737, +738, +739, +740, +741, +742, +743, +744, +745, +746, +747, +748, +749, +750, +751, +752, +753, +754, +755, +756, +757, +758, +759, +760, +761, +762, +763, +764, +765, +766, +767, +768, +769, +770, +771, +772, +773, +774, +775, +776, +777, +778, +779, +780, +781, +782, +783, +2177, +2178, +2179, +2180, +2181, +2182, +2183, +2184, +2185, +2186, +2187, +2188, +2189, +2190, +2191, +2192, +2193, +2194, +2195, +2196, +2197, +2198, +2199, +2200, +2201, +2202, +3140, +3141, +3142, +3143, +3144, +3145, +3146, +3147, +3148, +3149, +3150, +3151, +3152, +3153, +3154, +3155, +3156, +3157, +3158, +3159, +3160, +3161, +3162, +4109, +4110, +4111, +4112, +4113, +4114, +4115, +4116, +4117, +4118, +4119, +4120, +4121, +4122, +4123, +4124, +4125, +4126, +4127, +4128, +4129, +4130, +4131, +4132, +4133, +4134, +4135, +4136, +4137, +4138, +4139, +4140, +4141, +4142, +4143, +4144, +4145, -2173, -2172, -2171, -2170, -2169, -2168, -2167, -2166, -2165, -2164, -2163, -2162, -2161, -2160, -2159, -2158, -2157, -2156, -2155, -2154, -2153, -2152, -2151, -2150, -3221, -3220, -3219, -3218, -3217, -3216, -3215, -3214, -3213, -3212, -3211, -3210, -3209, -3208, -3207, -3206, -3205, -3204, -3203, +1652, +1653, +1654, +1655, +1656, +1657, +1658, +1659, +1660, +1661, +1662, +1663, +1664, +1665, +1666, +1667, +1668, +1669, +1670, +1671, +1672, +1673, +1674, +1675, +1676, +1677, +1678, +1679, +1680, +1681, +1682, +1683, +1684, +1685, +1686, +1687, +1688, +1689, +1690, +1691, +1692, +1693, +1694, +1695, +1696, +1697, +1698, +1699, -1075, -1074, -1073, -1072, -1071, -1070, -1069, -1068, -1067, -1066, -1065, -1064, -1063, -1062, -1061, -1060, -1059, -1058, -1057, -1056, -1055, -1054, -1053, -1052, -1051, -1050, -1049, -1048, -1047, -1046, -1045, -1044, -1043, -1042, -1041, -1040, -1039, -1038, -1037, -1036, -1035, -1034, -1033, -1032, -1031, -1030, -1029, -1028, -1027, -1026, -1025, -1024, -1023, -1022, -1021, -1020, -1019, -1018, -1017, -1016, -1015, -1014, -1013, -1012, -1011, -1010, -1009, -1008, -1007, -1006, -1005, -1004, -1003, -1002, -1001, -1000, -999, -998, -997, -996, -995, -994, -993, -992, -991, -990, -989, -988, -987, +3439, +3440, +3441, +3442, +3443, +3444, +3445, +3446, +3447, +3448, +3449, +3450, +3451, +3452, +3453, +3454, +3455, +3456, +3457, +3458, +3459, +3460, +3461, +3462, +3463, +3464, +3465, +3466, +3467, +3468, +3469, +3470, +3471, +3472, +3473, +3474, +3475, +3476, +3477, +3478, +3479, +3480, +3481, +3482, +3483, +3484, +3485, +3486, +3487, +3488, +3489, +3490, +3491, +3492, +3493, +3494, +3495, +3496, +3497, +3498, +3499, +3500, +3501, +3502, +3503, +3504, +3505, +3506, +3507, +3508, +3509, +3510, +3511, +3512, +3513, +3514, +3515, +3516, +3517, +3518, +3519, +3520, +3521, +3522, +3523, +3524, +3525, +3526, +3527, +3528, +3529, +3530, +3531, +3532, +3533, +3534, +3535, +3536, +3537, +3538, +3539, +3540, +3541, +3542, +3543, +3544, +3545, +3546, +3547, +3548, +3549, +3550, +3551, +3552, +3553, +3554, +3555, +3556, +3557, +3558, +3559, +3560, +3561, +3562, +3563, +3564, +3565, +3566, +3567, +3568, +3569, +3570, +3571, +3572, +3573, +3574, +3575, +3576, +3577, +3578, +3579, +3580, +3581, +3582, +3583, +3584, +3585, +3586, +3587, +3588, +3589, +3590, +3591, +3592, +3593, +3594, +3595, +3596, +3597, +3598, +3599, +3600, +3601, +3602, +3603, +3604, +3605, +3606, +3607, +3608, +3609, +3610, +3611, +3612, +3613, +3614, +3615, +3616, +3617, +3618, +3619, +3620, +3621, +3622, +3623, +3624, +3625, +3626, +3627, +3628, +3629, +3630, +3631, +3632, +3633, +3634, +3635, +3636, +3637, +3638, +3639, +3640, +3641, +3642, +3643, +3644, +3645, +3646, +3647, +3648, +3649, +3650, +3651, +3652, +3653, +3654, +3655, +3656, +3657, +3658, +3659, +3660, +3661, +3662, +3663, +3664, +3665, +3666, +3667, +3668, +3669, +3670, +3671, +3672, +3673, +3674, +3675, +3676, +3677, +3678, +3679, +3680, +3681, +3682, +3683, +3684, +3685, +3686, +3687, +3688, +3689, +3690, +3691, +3692, +3693, +3694, +3695, +3696, +3697, +3698, +3699, +3700, +3701, +3702, +3703, +3704, +3705, +3171, +3172, +3173, +3174, +3175, +3176, +3177, +3178, +3179, +3180, +3181, +3182, +3183, +3184, +3185, +3186, +3187, +3188, +3189, +3190, +3191, +3192, +3193, +3194, +3195, +3196, +3197, +3198, +3199, +3200, +3201, +3202, -1651, -1650, -1649, -1648, -1647, -1646, -1645, -1644, -1643, -1642, -1641, -1640, -1639, -1638, -1637, -1636, -1635, -1634, -1633, -1632, -1631, -1630, -1629, -1628, -1627, -1626, -1625, -1624, -1623, -1622, -1621, -1620, -1619, -1618, -1617, -1616, -1615, -1614, -1613, -1612, -1611, -1610, -1609, -1608, -1607, -1606, -1605, -1604, -1603, -1602, -1601, -1600, -1599, -1598, -1597, -1596, -1595, -1594, -1593, -1592, -1591, -1590, -1589, -1588, -1587, -1586, -1585, -1584, -1583, -1582, -1581, -1580, -1579, -1578, -1577, -1576, -1575, -1574, -1573, -1572, -1571, -1570, -1569, -1568, -1567, -1566, -1565, -1564, -1563, -1562, -1561, -1560, -1559, -1558, -1557, -1556, -1555, -1554, -1553, +3755, +3756, +3757, +3758, +3759, +3760, +3761, +3762, +3763, +3764, +3765, +3766, +3767, +3768, +3769, +3770, +3771, +3772, +3773, +3774, +3775, +3776, +3777, +3778, +3779, +3780, +3781, +3782, +3783, +3784, +3785, +3786, +3787, +3788, +3789, +3790, +3791, +3792, +3793, +3794, +3795, +3796, +3797, +3798, +3799, +3800, +3801, +3802, +3803, +3804, +3805, +3806, +3807, +3808, +3809, +3810, +3811, +3812, +3813, +3814, +3815, +3816, +3817, +3818, +3819, +3820, +3821, +3822, +3823, +3824, +3825, +3826, +3827, +3828, +3829, +3830, +3831, +3832, +3833, +3834, +3835, +3836, +3837, +3838, +3839, +3840, +3841, +3062, +3063, +3064, +3065, +3066, +3067, +3068, +3069, +3070, +3071, +3072, +3073, +3074, +3075, +3076, +3077, +3078, +3079, +3080, +3081, +3082, +3083, +3084, +3085, +3086, +3087, +3088, +3089, -3846, -3845, -3844, -3843, -3842, -3061, -3060, -3059, -3058, -3057, -3056, -3055, -3054, -3053, -3052, -3051, -3050, -3049, -3048, -3047, -3046, -3045, -3044, -3043, -3042, -3041, -3040, -3039, -3038, -3037, -3036, -3035, -3034, -3033, -3032, -3031, -3030, -3029, -3028, -3027, -3026, -3025, -3024, -3023, -3022, -3021, -3020, +2336, +2337, +2338, +2339, +2340, +2341, +2342, +2343, +2344, +2345, +2346, +2347, +2348, +2349, +2350, +2351, +2352, +2353, +2354, +2355, +2356, +2357, +2358, +2359, +2360, +2361, +2362, +2363, +2364, +2365, +2366, +2367, +2368, +2369, +2370, +2371, +2372, +2373, +2374, +2375, +2376, +2377, +2378, +2379, +2380, +2381, +2382, +2383, +2384, +2385, +2386, +2387, +2388, +2389, +2390, +2391, +2392, +2393, +2394, +2395, -2911, -2910, -2909, -2908, -2907, -2906, -2905, -2904, -2903, +2808, +2809, +2810, +2811, +2812, +2813, +2814, +2815, +2816, +2817, +2818, -1117, -1116, -1115, -1114, -1113, -1112, -1111, -1110, -1109, -1108, -1107, -1106, -1105, -1104, -1103, -1102, -1101, -1100, -1099, -1098, -1097, -1096, -1095, -1094, -1093, -1092, -1091, -1090, -1089, -1088, -1087, -1086, -1085, -1084, -1083, -1082, -1081, -1080, -1079, -1078, -1077, -1076, +1700, +1701, +1702, +1703, +1704, +1705, +1706, +1707, +1708, +1709, +1710, +1711, +1712, +1713, +1714, +1715, +1716, +1717, +1718, +1719, +1720, +1721, +1722, +1723, +1724, +1725, +1726, +1727, +1728, +1729, +1730, +1731, +1732, +1733, +1734, +1735, +1736, +1737, +1738, +1739, +1740, +1741, +1742, +1743, +1744, +1745, +1746, +1747, +1748, +1749, +1750, +1751, +1752, +1753, +1754, +1755, +1756, +1757, +1758, +1759, +1760, +1761, +1762, +1763, +1764, +1765, +1766, +1767, +1768, +1769, +1770, -2558, -2557, -2556, -2555, -2554, -2553, -2552, -2551, -2550, -2549, -2548, -2547, -2546, -2545, -2544, -2543, -2542, -2541, -2540, +3005, +3006, +3007, +3008, +3009, +3010, +3011, +3012, +3013, +3014, +3015, +3016, +3017, +3018, +3019, -2335, -2334, -2333, -2332, -2331, -2330, -2329, -2328, -2327, -2326, -2325, -2324, -2323, -2322, -2321, -2320, -2319, -2318, -2317, -2316, -2315, -2314, -2313, -2312, -2311, -2310, -2309, -2308, -2307, -2306, -2305, -2304, -2303, -2302, -2301, -2300, -2299, -2298, -2297, -2296, -2295, -2294, -2293, -2292, -2291, -2290, -2289, -2288, -2287, -2286, -2285, -2284, -2283, -2282, -2281, -2280, -2279, -2278, -2277, -2276, -2275, -2274, -2273, -2272, -2271, -2270, -2269, -2268, -2267, -2266, -2265, -2264, -2263, -2262, -2261, -2260, -2259, -2258, -2257, -2256, -2255, -2254, -2253, -2252, -2251, -2250, -2249, -2248, -2247, -2246, -2245, -2244, -2243, +4063, +4064, +4065, +4066, +4067, +4068, +4069, +4070, +4071, +4072, +4073, +4074, +4075, +4076, +4077, +4078, +4079, +4080, +4081, +4082, +4083, +4084, +4085, -4445, -4444, -4443, -4442, -4441, -4440, -4439, -4438, -4437, -4436, -4435, -4434, -4433, -4432, -4431, +4028, +4029, +4030, +2140, +2141, +2142, +2143, +2144, +2145, +2146, +2147, +2148, +2149, +3222, +3223, +3224, +3225, +3226, +3227, +3228, +3229, +3230, +3231, +3232, +3233, +3234, +3235, +3236, +3237, +3238, +3239, +3240, +3241, +3242, +3243, +3244, +3245, +3246, +3247, +3248, +3249, +3250, +3251, +3252, +3253, +3254, +3255, +3256, +3257, +3258, +3259, +3260, +3261, +3262, +3263, +3264, +3265, +3266, +3267, +3268, +3269, +3270, +3271, +3272, +3273, +3274, +3275, +3276, +3277, +3278, +3279, +3280, +3281, +3282, +3283, +3284, +3285, +3286, +3287, +3288, +3289, +3290, +3291, +3292, +3293, +3294, +3295, +3296, +3297, +3298, +3299, +3300, +3301, +3302, +3303, +3304, +3305, +3306, +3307, +3308, +3309, +3310, +3311, +3312, +3313, +3314, +3315, +3316, +3317, +3318, +3319, +3320, +3321, +3322, +3323, +3324, +3325, +3326, +3327, +3328, +3329, +3330, +3331, +3332, +3333, +3334, +3335, +3336, +3337, +3338, +3339, +2039, +2040, +2041, +2042, +2043, +2044, +2045, +2046, +2047, +2048, +2049, +2050, +2051, +2052, +2053, +2054, +2055, +2056, +2057, +2058, +2059, +2060, +2061, +2062, +2063, +2064, +2065, +2066, +2067, +2068, +2069, +2070, +2071, +2072, +2073, +2074, +2075, +2076, +2077, +2078, +2079, +2080, +2081, +2082, +2083, +2084, +2085, +2086, +2087, +2088, +2089, +2090, +2091, +2092, +2093, +2094, +2095, +2096, +2097, +2098, +2099, +2100, +2101, +2102, +2103, +2104, +2105, +2106, +2107, +2108, +2109, +2110, +2111, +2112, +276, +277, +278, +279, +280, +281, +282, +283, +284, +285, +286, +287, +288, +289, +290, +291, +292, +293, +294, +295, +296, +297, +298, +299, +300, +301, +302, +303, +304, +305, +306, +307, +308, +309, +310, +311, +312, +313, +314, +315, +316, +317, +318, +319, +320, +321, +322, +323, +324, +325, +326, +327, +328, +329, +330, +331, +332, +333, +334, +335, +336, +337, +338, +339, +340, +341, +342, +343, +344, +345, +346, +347, +348, +349, +350, +351, +352, +353, +354, +355, +356, +357, +358, +359, +360, +361, +362, +363, +364, +365, +366, +367, +368, +369, +370, +371, +372, +373, +374, +375, +376, +377, +378, +379, +380, +381, +382, +383, +384, +385, +386, +387, +388, +389, +390, +391, +392, +393, +394, +395, +396, +397, +398, +399, +400, +401, +402, +403, +404, +405, +406, +407, +408, +409, +410, +411, +412, +413, +414, +415, +416, +417, +418, +419, +420, +421, +422, +423, +424, +425, +426, +427, +428, +429, +430, +431, +432, +433, +434, +435, +436, +437, +438, +439, +1258, +1259, +1260, +1261, +1262, +1263, +1264, +1265, +1266, +1267, +1268, +1269, +1270, +1271, +1272, +1273, +1274, +1275, +1276, +1277, +1278, +1279, +1280, +1281, +1282, +1283, +1284, +1285, +1286, +1287, +1288, +1289, +1290, +1291, +1292, +1293, +1294, +1295, +1296, +1297, +1298, +1299, +1300, +1301, +1302, +1303, +1304, +1305, +1306, +1307, +1308, +1309, +1310, +1311, +1312, +1313, +1314, +1315, +1316, +1317, +1318, +1319, +1320, +1321, +1322, +1323, +1324, +1325, +1326, +1327, +1328, +1329, +1330, +1331, +1332, +1333, -4346, -4345, -4344, -4343, -4342, -4341, -4340, -4339, -4338, -4337, -4336, -4335, -4334, -4333, -4332, -4331, -4330, -4329, -4328, -4327, -4326, -4325, -4324, -4323, -4322, -4321, -4320, -4319, -4318, -4317, -4316, -4315, -4314, -4313, -4312, -4311, -4310, -4309, -4308, -4307, -4306, -4305, -4304, -4303, -4394, -4393, -4392, +4270, +4271, +4272, +4273, +4274, +4275, +4276, +4277, +4278, +4279, +4280, +4281, +4282, +4283, +4284, +4285, +4286, +4287, +4288, +4289, +4290, +4291, +4292, +4293, +4294, +4295, +4296, +4297, +4298, +4299, +4300, +4301, +4302, +4395, +4396, +4397, +4398, +4399, +4400, +4401, +4402, +4403, +4404, +4405, +4406, +4407, +2832, +2833, +2834, +51, +52, +53, +54, +55, +56, +57, +58, +59, +60, +61, +62, +63, +64, +65, +66, +67, +68, +69, +70, +71, +72, +73, +74, +75, +76, -560, -559, -558, -557, -556, -555, -554, -553, -552, -551, -550, -549, -548, -547, -546, -545, -544, -543, -542, -541, -540, -539, -538, -537, -536, -535, -534, -533, -532, -531, -530, -529, -528, -527, -526, -525, -524, -523, -522, -521, -520, -519, -518, -517, -516, -515, -514, -513, -512, -511, -510, -509, -508, -507, -506, -505, -504, -503, -502, -501, -500, -499, -498, -497, -496, -495, -494, -493, -492, -491, -490, -489, -488, -487, -486, -485, -484, -483, -482, -481, -480, -479, -478, -477, -476, -475, -474, -473, -472, -471, -470, -469, -468, -467, -466, -465, -464, -463, -462, -461, -460, -459, -458, -457, -456, -455, -454, -453, -452, -451, -450, -449, -448, -447, -446, +926, +927, +928, +929, +930, +931, +932, +933, +934, +935, +936, +937, +938, +939, +940, +941, +942, +943, +944, +945, +946, +947, +948, +949, +950, +951, +952, +953, +954, +955, +956, +957, +958, +959, +960, +961, +962, +963, +964, +965, +966, +967, +968, +969, +970, +971, +972, +973, +974, +975, +976, +977, +978, +979, +980, +981, +982, +983, +984, +985, +986, -3438, -3437, -3436, -3435, -3434, -3433, -3432, -3431, -3430, -3429, -3428, -3427, -3426, -3425, -3424, -3423, -3422, -3421, -3420, -3419, -3418, -3417, -3416, -3415, -3414, -3413, -3412, -3411, -3410, -3409, -3408, -3407, -3406, -3405, -3404, -3403, -3402, -3401, -3400, -3399, -3398, -3397, -3396, -3395, -3394, -3393, -3392, -3391, -3390, -3389, -3388, -3387, -3386, -3385, -3384, -3383, -3382, -3381, -3380, -3379, -3378, -3377, -3376, -3375, -3374, -3373, -3372, -3371, -3370, -3369, -3368, -3367, -3366, -3365, -3364, -3363, -3362, -3361, -3360, -3359, -3358, -3357, -3356, -3355, -3354, -3353, -3352, -3351, -3350, -3349, -3348, -3347, -3346, -3345, -3344, -3343, -3342, -3341, -3340, -2038, -2037, -2036, -2035, -2034, -2033, -2032, -2031, -2030, -2029, -2028, -2027, -2026, -2025, -2024, -2023, -2022, -2021, -2020, -2019, -2018, -2017, -2016, -2015, -2014, -2013, -2012, -2011, -2010, -2009, -2008, -2007, -2006, -2005, -2004, -2003, -2002, -2001, -2000, -1999, -1998, -1997, -1996, -1995, -1994, -1993, -1992, -1991, -1990, -1989, -1988, -1987, -1986, -1985, -1984, -1983, -1982, -1981, -1980, -1979, -1978, -1977, -1976, -1975, -1974, -1973, -1972, -1971, -1970, -1969, -1968, -1967, -1966, -1965, -1964, -1963, -1962, -1961, -1960, -1959, -1958, -1957, -1956, -1955, -1954, -1953, -1952, -1951, -1950, -1949, -1948, -1947, -1946, -1945, -1944, -1943, -1942, -1941, -1940, -1939, -1938, -1937, -1936, -1935, -1934, -1933, -1932, -1931, -1930, -1929, -1928, -1927, -1926, -1925, -1924, -1923, -1922, -1921, -1920, -1919, -1918, -1917, -1916, -1915, -1914, -1913, -1912, -1911, -1910, -1909, -1908, -1907, -1906, -1905, -1904, -1903, -1902, -1901, -1900, -1899, -1898, -1897, -1896, -1895, -1894, -1893, -1892, -1891, -1890, -1889, -1888, -1887, -1886, -1885, -1884, -1883, -1882, -1881, -1880, -1879, -1878, -1877, -1876, -1875, -1874, -1873, -1872, -1871, -1870, -1869, -1868, -1867, -1866, -1865, -1864, -1863, -1862, -1861, -1860, -1859, -1858, -1857, -1856, -1855, -1854, -1853, -1852, -1851, -1850, -1849, -1848, -1847, -1846, -1845, -1844, -1843, -1842, -1841, -1840, -1839, -1838, -1837, -1836, -1835, -1834, -1833, -1832, -1831, -1830, -1829, -1828, -1827, -1826, +2400, +2401, +2402, +2403, +2404, +2405, +2406, +2407, +2408, +2409, +2410, +2411, +2412, +2413, +2414, +2415, +2416, +2417, +2418, +2419, -2492, -2491, -2490, -2489, -2488, -2487, -2486, -2485, -2484, -2483, -2482, -2481, -2480, -2479, -2478, -2477, -2476, -2475, -2474, -2473, -2472, -2471, -2470, -2469, -2468, -2467, -2466, -2465, -2464, -2463, -2462, -2461, -2460, -2459, -2458, -2457, -2456, -2455, -2454, -2453, -2452, -2451, -2450, -2449, -2448, -2447, -2446, -2445, -2444, -2443, -2442, -2441, -2440, -2439, -2438, -2437, -2436, -2435, -2434, -2433, -2432, -2431, -2430, -2429, -2428, -2427, -2426, -2425, -2424, -2423, -2422, -2421, -2420, +2493, +2494, +2495, +2496, +2497, +2498, +2499, +2500, +2501, +2502, +2503, +2504, +2505, +2506, +2507, +2508, +2509, +2510, +2511, +2512, +2513, +2514, +2515, +2516, +2517, +2518, +2519, +2520, +2521, +2522, +2523, +2524, +2525, +2526, +2527, +2528, +2529, +2530, +2531, +2532, +2533, +2534, +2535, +2536, +2537, +2538, +2539, -3004, -3003, -3002, -3001, -3000, -2999, -2998, -2997, -2996, -2995, -2994, -2993, -2992, -2991, -2990, -4424, -4423, -4422, -4421, -4420, -4419, -4418, -4417, -4416, -4415, -4414, -4413, -4412, -4411, -4410, -4409, -4408, -2831, -2830, -2829, -2828, -2827, -2826, -2825, -2824, -2823, -2822, -2821, -2820, -2819, +1118, +1119, +1120, +1121, +1122, +1123, +1124, +1125, +1126, +1127, +1128, +1129, +1130, +1131, +1132, +1133, +1134, +1135, +1136, +1137, +1138, +1139, +1140, +1141, +1142, +1143, +1144, +1145, +1146, +1147, +1148, +1149, +1150, +1151, +1152, +1153, +1154, +1155, +1156, +1157, +1158, +1159, +1160, +1161, +1162, +1163, +1164, +1165, +1166, +1167, +1168, +1169, +1170, +1171, +1172, +1173, +1174, +1175, +1176, +1177, +1178, +1179, +1180, +1181, +1182, +1183, +1184, +1185, +1186, +1187, +1188, +1189, +1190, +1191, +1192, +1193, +1194, +1195, +1196, +1197, +1198, +1199, +1200, +1201, +1202, +1203, +1204, +1205, +1206, +1207, +1208, +1209, +1210, +1211, +1212, +1213, +1214, +1215, +1216, +1217, +1218, +1219, +1220, +1221, +1222, +1223, +1224, +1225, +1226, +1227, +1228, +1229, +1230, +1231, +1232, +1233, +1234, +1235, +1236, +1237, +1238, +1239, +1240, +1241, +1242, +1243, +1244, +1245, +1246, +1247, +1248, +1249, +1250, +1251, +1252, +1253, +1254, +1255, +1256, +1257, +440, +441, +442, +443, +444, +445, -925, -924, -923, -922, -921, -920, -919, -918, -917, -916, -915, -914, -913, -912, -911, -910, -909, -908, -907, -906, -905, -904, -903, -902, -901, -900, -899, -898, -897, -896, -895, -894, -893, -892, -891, -890, -889, -888, -887, -886, -885, -884, -883, -882, -881, -880, -879, -878, -877, -876, -875, -874, -873, -872, -871, -870, -869, -868, -867, -866, -865, -864, -863, -862, -861, -860, -859, -858, -857, -856, -855, -854, -853, -852, -851, -850, -849, -848, -847, -846, -845, -844, -843, -842, -841, -840, -839, -838, -837, -836, -835, -1505, -1504, -1503, -1502, -1501, -1500, -1499, -1498, -1497, -1496, -1495, -1494, -1493, -1492, -1491, -1490, -1489, -1488, -1487, -1486, -1485, -1484, -1483, -1482, -1481, -1480, -1479, -1478, -1477, -1476, -1475, -1474, -1473, -1472, -1471, -1470, -1469, -1468, -4025, -4024, -4023, -4022, -4021, -4020, +4516, +4517, +4518, +4519, +4520, +4521, +4522, +4523, +4524, +4525, +4526, +4527, +4528, +4529, +4530, +4531, +4532, +4533, +4534, +4535, +4536, +4537]) )
