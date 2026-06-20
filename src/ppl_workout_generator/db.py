# 1. Exercise Database
EXERCISE_DB = [
    # === PUSH DAY - Chest, Shoulders, Triceps ===
    {"name": "Bench Press", "split": "push", "muscle": "chest", "type": "compound", "description": "Lie flat on a bench, grip the barbell slightly wider than shoulder-width, lower it to your chest, and press up explosively."},
    {"name": "Incline Dumbbell Press", "split": "push", "muscle": "chest", "type": "compound", "description": "Set an incline bench to 30-45 degrees. Press dumbbells vertically to heavily target the upper chest fibers."},
    {"name": "Decline Bench Press", "split": "push", "muscle": "chest", "type": "compound", "description": "Use a decline bench to target the lower chest. Lower the bar to your chest and press up with control."},
    {"name": "Chest Dips", "split": "push", "muscle": "chest", "type": "compound", "description": "Lean slightly forward on parallel bars, lower until your shoulders are below your elbows, then push back up."},
    {"name": "Cable Flyes", "split": "push", "muscle": "chest", "type": "isolation", "description": "Bring cables together in a smooth hugging motion, focusing on a deep contraction at the center of the chest."},
    {"name": "Pec Deck Machine", "split": "push", "muscle": "chest", "type": "isolation", "description": "Sit in the machine and bring the pads together in front of your chest, squeezing hard at the peak contraction."},
    
    {"name": "Overhead Press", "split": "push", "muscle": "shoulders", "type": "compound", "description": "Press a barbell overhead from shoulder level while standing, keeping your core and glutes tightly braced."},
    {"name": "Arnold Press", "split": "push", "muscle": "shoulders", "type": "compound", "description": "Start with palms facing you at shoulder height, press up while rotating palms forward to fully target all deltoid heads."},
    {"name": "Seated Dumbbell Press", "split": "push", "muscle": "shoulders", "type": "compound", "description": "Sit on a bench with back support and press dumbbells overhead."},
    {"name": "Lateral Raises", "split": "push", "muscle": "shoulders", "type": "isolation", "description": "Raise dumbbells out to your sides up to shoulder height to isolate and widen the lateral deltoid heads."},
    {"name": "Front Raises", "split": "push", "muscle": "shoulders", "type": "isolation", "description": "Raise dumbbells or a plate straight in front of you to shoulder height, targeting the anterior deltoids."},
    {"name": "Rear Delt Flyes", "split": "push", "muscle": "shoulders", "type": "isolation", "description": "Bend over or use a machine to fly dumbbells out to the sides, targeting the rear deltoids."},
    
    {"name": "Tricep Pushdowns", "split": "push", "muscle": "triceps", "type": "isolation", "description": "Using a cable machine, pin your elbows to your sides and fully extend your arms downward to lock out the triceps."},
    {"name": "Skull Crushers", "split": "push", "muscle": "triceps", "type": "isolation", "description": "Lie down, lower an EZ-bar towards your forehead by bending only at the elbows, then extend back up."},
    {"name": "Overhead Tricep Extension", "split": "push", "muscle": "triceps", "type": "isolation", "description": "Hold a dumbbell or EZ-bar overhead with both hands and lower it behind your head by bending at the elbows."},
    {"name": "Close-Grip Bench Press", "split": "push", "muscle": "triceps", "type": "compound", "description": "Use a narrower grip on the barbell to shift emphasis from chest to triceps during the press."},
    {"name": "Tricep Kickbacks", "split": "push", "muscle": "triceps", "type": "isolation", "description": "Hinge forward and extend your arms back while holding dumbbells, focusing on the squeeze at the top."},

    # === PULL DAY - Back, Rear Shoulders, Biceps, Traps ===
    {"name": "Deadlift", "split": "pull", "muscle": "back", "type": "compound", "description": "Lift a loaded barbell off the ground to hip level, driving through your heels and engaging your entire posterior chain."},
    {"name": "Pull-Ups", "split": "pull", "muscle": "back", "type": "compound", "description": "Hang from a bar with palms facing away and pull your chest toward the bar. Use assistance if needed."},
    {"name": "Chin-Ups", "split": "pull", "muscle": "back", "type": "compound", "description": "Perform pull-ups with palms facing you to increase biceps involvement."},
    {"name": "Lat Pulldown", "split": "pull", "muscle": "back", "type": "compound", "description": "Pull the overhead bar down to your upper chest while focusing on squeezing your shoulder blades down and back."},
    {"name": "Barbell Row", "split": "pull", "muscle": "back", "type": "compound", "description": "Hinge forward at the hips and pull the barbell towards your lower belly button, driving backwards with your elbows."},
    {"name": "Seated Cable Row", "split": "pull", "muscle": "back", "type": "compound", "description": "Sit at the cable row station, pull the handle toward your torso while squeezing your shoulder blades together."},
    {"name": "Single-Arm Dumbbell Row", "split": "pull", "muscle": "back", "type": "compound", "description": "Brace on a bench and row a dumbbell up toward your hip, one arm at a time."},
    {"name": "T-Bar Row", "split": "pull", "muscle": "back", "type": "compound", "description": "Straddle the T-bar and row the weight toward your chest with a neutral grip."},
    
    {"name": "Face Pulls", "split": "pull", "muscle": "shoulders", "type": "isolation", "description": "Pull a cable rope toward your nose, flaring your elbows out to isolate the rear delts and rotator cuffs."},
    {"name": "Shrugs", "split": "pull", "muscle": "traps", "type": "isolation", "description": "Hold heavy dumbbells or a barbell and shrug your shoulders upward as high as possible."},
    {"name": "Barbell Shrugs", "split": "pull", "muscle": "traps", "type": "isolation", "description": "Use a barbell behind your back or in front to target the upper traps."},
    
    {"name": "Bicep Barbell Curls", "split": "pull", "muscle": "biceps", "type": "isolation", "description": "Stand tall and curl the barbell upward towards your shoulders, keeping your elbows locked firmly at your sides."},
    {"name": "Hammer Curls", "split": "pull", "muscle": "biceps", "type": "isolation", "description": "Curl dumbbells with a neutral (hammer) grip to target the brachialis and outer biceps."},
    {"name": "Preacher Curls", "split": "pull", "muscle": "biceps", "type": "isolation", "description": "Use a preacher bench to isolate the biceps and eliminate momentum."},
    {"name": "Concentration Curls", "split": "pull", "muscle": "biceps", "type": "isolation", "description": "Sit on a bench, rest your elbow on your inner thigh, and curl one dumbbell at a time."},
    {"name": "Cable Bicep Curls", "split": "pull", "muscle": "biceps", "type": "isolation", "description": "Use a straight bar or rope attachment on the cable machine for constant tension."},

    # === LEGS DAY - Quads, Hamstrings, Glutes, Calves ===
    {"name": "Barbell Squat", "split": "legs", "muscle": "quads", "type": "compound", "description": "Rest a barbell across your upper back, drop your hips until thighs are parallel to the floor, and drive back up."},
    {"name": "Leg Press", "split": "legs", "muscle": "quads", "type": "compound", "description": "Place feet shoulder-width on the platform and press the weight away by extending your knees and hips."},
    {"name": "Bulgarian Split Squat", "split": "legs", "muscle": "quads", "type": "compound", "description": "Rear foot elevated on a bench, lower your front thigh until parallel to the floor."},
    {"name": "Leg Extensions", "split": "legs", "muscle": "quads", "type": "isolation", "description": "Extend your legs against the pad to isolate and build the quadriceps."},
    {"name": "Goblet Squat", "split": "legs", "muscle": "quads", "type": "compound", "description": "Hold a dumbbell at chest level and squat deep, keeping your torso upright."},
    
    {"name": "Romanian Deadlift", "split": "legs", "muscle": "hamstrings", "type": "compound", "description": "Hinge at your hips while keeping your back flat, lowering the bar down your shins to deeply stretch the hamstrings."},
    {"name": "Leg Curls", "split": "legs", "muscle": "hamstrings", "type": "isolation", "description": "Lie or sit in the machine and pull the heel pad firmly toward your glutes to isolate the hamstrings."},
    {"name": "Nordic Hamstring Curls", "split": "legs", "muscle": "hamstrings", "type": "isolation", "description": "Kneel and lower your body forward slowly while keeping hips extended, then push back up."},
    
    {"name": "Hip Thrusts", "split": "legs", "muscle": "glutes", "type": "compound", "description": "Place upper back on a bench, drive hips upward with a barbell across your pelvis for powerful glute activation."},
    {"name": "Glute Bridge", "split": "legs", "muscle": "glutes", "type": "compound", "description": "Lie on the floor and thrust hips upward, squeezing glutes at the top."},
    {"name": "Cable Kickbacks", "split": "legs", "muscle": "glutes", "type": "isolation", "description": "Attach ankle strap and kick one leg back while keeping the movement controlled."},
    
    {"name": "Standing Calf Raises", "split": "legs", "muscle": "calves", "type": "isolation", "description": "Rise onto your toes with a barbell or machine, fully contracting the calves at the top."},
    {"name": "Seated Calf Raises", "split": "legs", "muscle": "calves", "type": "isolation", "description": "Target the soleus muscle by performing calf raises with knees bent."},
    {"name": "Donkey Calf Raises", "split": "legs", "muscle": "calves", "type": "isolation", "description": "Bend forward and raise onto your toes to hit the calves from a stretched position."},
]