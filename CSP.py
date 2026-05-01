from ortools.sat.python import cp_model

model = cp_model.CpModel()

alice = model.new_int_var(0,2,'alice')
bob = model.new_int_var(0,2,'bob')
charlie = model.new_int_var(0,2,'charlie')

model.add_all_different([alice,bob,charlie])
model.add(alice != 0)

solver = cp_model.CpSolver()
results = solver.solve(model)

if results == cp_model.FEASIBLE or results == cp_model.OPTIMAL:
    shifts = ['Morning','Afternoon','Evening']
    print("alice: ",shifts[solver.value(alice)])
    print("bob: ",shifts[solver.value(bob)])
    print("charlie: ",shifts[solver.value(charlie)])
