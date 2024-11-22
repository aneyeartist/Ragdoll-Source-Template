import bpy

def rename_bones():
    
    dict = {
        "spine1":      "bip_pelvis",
        "spine.001":       "bip_spine_0",
        "spine.002":      "bip_spine_1",
        "spine.003":      "bip_spine_2",
        "spine.004":      "bip_neck_0",
        "spine.005":       "bip_neck_1",
        "spine.006":       "bip_head",

        "pelvis.L":     "bip_pelvis_L",
        "pelvis.R":     "bip_pelvis_R",
        
        "shoulder.R":   "bip_shoulder_R",   
        "upper_arm.R":   "bip_upperArm_R",   
        "forearm.R":    "bip_lowerArm_R",
        "hand.R":       "bip_hand_R",

        "thigh.R":     "bip_hip_R",
        "shin.R":      "bip_knee_R",
        "foot.R":      "bip_foot_R",
        "toe.R":      "bip_toe_R",
        
        "pinky.01.R":   "bip_pinky_0_R",
        "pinky.02.R":  "bip_pinky_1_R",
        "pinky.03.R":  "bip_pinky_2_R",
        "ring.01.R":   "bip_ring_0_R",
        "ring.02.R":  "bip_ring_1_R",
        "ring.03.R":  "bip_ring_2_R",
        "middle.01.R":   "bip_middle_0_R",
        "middle.02.R":  "bip_middle_1_R",
        "middle.03.R":  "bip_middle_2_R",
        "index.01.R":   "bip_index_0_R",
        "index.02.R":  "bip_index_1_R",
        "index.03.R":  "bip_index_2_R",
        "thumb.01.R":   "bip_thumb_0_R",
        "thumb.02.R":  "bip_thumb_1_R",
        "thumb.03.R":  "bip_thumb_2_R",
        
        "shoulder.L":   "bip_shoulder_L",   
        "upper_arm.L":   "bip_upperArm_L",   
        "forearm.L":    "bip_lowerArm_L",
        "hand.L":       "bip_hand_L",

        "thigh.L":     "bip_hip_L",
        "shin.L":      "bip_knee_L",
        "foot.L":      "bip_foot_L",
        "toe.L":      "bip_toe_L",
        
        "pinky.01.L":   "bip_pinky_0_L",
        "pinky.02.L":  "bip_pinky_1_L",
        "pinky.03.L":  "bip_pinky_2_L",
        "ring.01.L":   "bip_ring_0_L",
        "ring.02.L":  "bip_ring_1_L",
        "ring.03.L":  "bip_ring_2_L",
        "middle.01.L":   "bip_middle_0_L",
        "middle.02.L":  "bip_middle_1_L",
        "middle.03.L":  "bip_middle_2_L",
        "index.01.L":   "bip_index_0_L",
        "index.02.L":  "bip_index_1_L",
        "index.03.L":  "bip_index_2_L",
        "thumb.01.L":   "bip_thumb_0_L",
        "thumb.02.L":  "bip_thumb_1_L",
        "thumb.03.L":  "bip_thumb_2_L",
        
    }
    
    for b in bpy.context.object.data.bones:
        if b.name in dict.keys():
            b.name = dict[b.name]

rename_bones()

