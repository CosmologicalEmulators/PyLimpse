from juliacall import Main as jl

jl.seval("using Limpse")
jl.seval("using SimpleChains")
jl.seval("using BSON")
jl.seval("using Static")

limpse_compute_Pk = jl.seval('Limpse.compute_Pk')
load_emu = jl.seval('Limpse.load_emulators')

def compute_Pk(input_test, emu):
    Pk = limpse_compute_Pk(jl.collect(input_test), emu)
    return Pk

