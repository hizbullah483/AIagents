from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model =DiscreteBayesianNetwork([('Rain','Sprinkler'),('Rain','WetGrass'),('Sprinkler','WetGrass')])


riskofrain = TabularCPD(variable='Rain', variable_card=2,
                        values=[[0.8], #false
                                [0.2]]) #true

riskofsprinkler = TabularCPD(variable='Sprinkler',variable_card=2,
                             values=[[0.6,0.99], #off ((0.6 if no rain, 0.99 if rain)
                                     [0.4,0.01]], #on (0.4 if no rain, 0.01 if rain)
                            evidence=['Rain'], evidence_card=[2]) 

riskofwg = TabularCPD(variable='WetGrass',variable_card=2,
                      values=[[1,0.1,0.1,0.01], #dry. (R,S): FF,FT,TF,TT
                              [0,0.9,0.9,0.99]], #Wet. (R,S) FF,FT,TF,TT
                    evidence=['Rain','Sprinkler'],
                    evidence_card=[2,2]
                    )

model.add_cpds(riskofrain,riskofsprinkler,riskofwg)
model.check_model()
infer = VariableElimination(model)
result = infer.query(variables=['Rain'],evidence={'WetGrass' : 1})
print(result)

