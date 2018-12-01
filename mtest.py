from OCC.gp import gp_Trsf, gp_Vec

def vals(mm):
    return [mm.Value(r, c) for r in range(1,4) for c in range(1,5)]


m = gp_Trsf()

print(vals(m))


v = gp_Vec(1,2,3)
m.SetTranslation(v)