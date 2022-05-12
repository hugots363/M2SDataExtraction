import sys

print("EMPEZANDO EXTRACCION BASELINE")
script_descriptor = open("agruparUnificada.py")
miss_hits_amontonado_absoluto = script_descriptor.read()
sys.argv = ["ejecucion_amontonados.py","/home/hutarsan/Documentos/racetrack/reports/cache_unificada_def/bline_L2_128kb_8v/reps/", "/home/hutarsan/Documentos/racetrack/scripts/bline_L2_128kb_8v.csv", "2" ]
exec(miss_hits_amontonado_absoluto)
script_descriptor.close()

script_descriptor = open("agruparUnificada.py")
miss_hits_amontonado_absoluto = script_descriptor.read()
sys.argv = ["ejecucion_amontonados.py","/home/hutarsan/Documentos/racetrack/reports/cache_unificada_def/bline_L2_256kb_8v/reps/", "/home/hutarsan/Documentos/racetrack/scripts/bline_L2_256kb_8v.csv", "2" ]
exec(miss_hits_amontonado_absoluto)
script_descriptor.close()

script_descriptor = open("agruparUnificada.py")
miss_hits_amontonado_absoluto = script_descriptor.read()
sys.argv = ["ejecucion_amontonados.py","/home/hutarsan/Documentos/racetrack/reports/cache_unificada_def/bline_L2_512kb_8v/reps/", "/home/hutarsan/Documentos/racetrack/scripts/bline_L2_512kb_8v.csv", "2" ]
exec(miss_hits_amontonado_absoluto)
script_descriptor.close()

print("EMPEZANDO EXTRACCION ISOAREA")

script_descriptor = open("agruparUnificada.py")
miss_hits_amontonado_absoluto = script_descriptor.read()
sys.argv = ["ejecucion_amontonados.py","/home/hutarsan/Documentos/racetrack/reports/cache_unificada_def/isoArea_1536kb_L1_3w/reps/", "/home/hutarsan/Documentos/racetrack/scripts/isoArea_1536kb_L1_3w.csv", "2" ]
exec(miss_hits_amontonado_absoluto)
script_descriptor.close()

script_descriptor = open("agruparUnificada.py")
miss_hits_amontonado_absoluto = script_descriptor.read()
sys.argv = ["ejecucion_amontonados.py","/home/hutarsan/Documentos/racetrack/reports/cache_unificada_def/isoArea_2560kb_L1_5w/reps/", "/home/hutarsan/Documentos/racetrack/scripts/isoArea_2560kb_L1_5w.csv", "2" ]
exec(miss_hits_amontonado_absoluto)
script_descriptor.close()

script_descriptor = open("agruparUnificada.py")
miss_hits_amontonado_absoluto = script_descriptor.read()
sys.argv = ["ejecucion_amontonados.py","/home/hutarsan/Documentos/racetrack/reports/cache_unificada_def/isoArea_5120kb_L1_10w/reps/", "/home/hutarsan/Documentos/racetrack/scripts/isoArea_5120kb_L1_10w.csv", "2" ]
exec(miss_hits_amontonado_absoluto)
script_descriptor.close()


print("EMPEZANDO EXTRACCION ISOCAPACITY")

script_descriptor = open("agruparUnificada.py")
miss_hits_amontonado_absoluto = script_descriptor.read()
sys.argv = ["ejecucion_amontonados.py","/home/hutarsan/Documentos/racetrack/reports/cache_unificada_def/isoCapacity_160kb_L1_5w/reps/", "/home/hutarsan/Documentos/racetrack/scripts/isoCapacity_160kb_L1_5w.csv", "2" ]
exec(miss_hits_amontonado_absoluto)
script_descriptor.close()

script_descriptor = open("agruparUnificada.py")
miss_hits_amontonado_absoluto = script_descriptor.read()
sys.argv = ["ejecucion_amontonados.py","/home/hutarsan/Documentos/racetrack/reports/cache_unificada_def/isoCapacity_288kb_L1_9w/reps/", "/home/hutarsan/Documentos/racetrack/scripts/isoCapacity_288kb_L1_9w.csv", "2" ]
exec(miss_hits_amontonado_absoluto)
script_descriptor.close()

script_descriptor = open("agruparUnificada.py")
miss_hits_amontonado_absoluto = script_descriptor.read()
sys.argv = ["ejecucion_amontonados.py","/home/hutarsan/Documentos/racetrack/reports/cache_unificada_def/isoCapacity_544kb_L1_17w/reps/", "/home/hutarsan/Documentos/racetrack/scripts/isoCapacity_544kb_L1_17w.csv", "2" ]
exec(miss_hits_amontonado_absoluto)
script_descriptor.close()

print("EMPEZANDO COMPARATIVA NO INTERLEAVING")

script_descriptor = open("agruparUnificada.py")
miss_hits_amontonado_absoluto = script_descriptor.read()
sys.argv = ["ejecucion_amontonados.py","/home/hutarsan/Documentos/racetrack/reports/cache_unificada_def/isoCapacity_160kb_L1_5w_noInter/reps/", "/home/hutarsan/Documentos/racetrack/scripts/isoCapacity_160kb_L1_5w_noInter.csv", "2" ]
exec(miss_hits_amontonado_absoluto)
script_descriptor.close()

print("ACABADO!")