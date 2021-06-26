# %%
from optimization import *
from simulation import *
import os.path
import sys
from matplotlib import pyplot as plt

# Read Data
my_path = os.path.dirname(__file__)
input_data = read_data(os.path.join(my_path, 'Data', 'Data.xlsx'))
# %% Optimization
# No need to do an expected state simulation, 
# because setting values to extremes gives same results

# for cw_p in [1, 1.25, 1.5]:
#     for cs_p in [1, 1.25, 1.5]:
#         for cc_p in [1, 25, 50]:

            # if cw_p == 1.0 and cs_p == 1.0:
            #     continue
            # input_data.model_param.cw = cw_p
            # input_data.model_param.cs = cs_p
            # input_data.model_param.cc = cc_p

# print(f"\t\tcw {cw_p}-cs {cs_p}-cc {cc_p}")
# print(input_data.)

# Phase 1
init_state, init_action = generate_initial_state_action(input_data)
state_action_list = [(init_state, init_action)]
feasible_list = generate_feasible_sa_list(input_data, state_action_list)

# Phase 2
optimal_list, betas = generate_optimal_sa_list(input_data, feasible_list)
export_betas(betas, os.path.join(my_path, 'Data', f'Optimal-Betas-ZeroVariation.xlsx'))
            


# %% Compare Policies
# Import betas
fig, axes = plt.subplots(1, 1)
# fig.set_size_inches()
# fig.subplots_adjust(top = 1.5)

# counter = 0
# for cw_p in [1, 1.25, 1.5]:
#     for cs_p in [1, 1.25, 1.5]:
#         for cc_p in [1, 25, 50]: 
betas = read_betas(os.path.join(my_path, 'Data', f'Optimal-Betas-ZeroVariation.xlsx'))

# input_data.model_param.cw = cw_p
# input_data.model_param.cs = cs_p
# input_data.model_param.cc = cc_p

# print(f'COSTS: cw - {cw_p}, cs - {cs_p}, cc - {cc_p}')
# betas = read_betas(os.path.join(my_path, 'Data', 'Optimal-Betas.xlsx'))

# Compare Policies
compare_policies(input_data, betas, 5, 3000, 1500, axes)
# axes[counter].set_title(f'COSTS: cw - {cw_p}, cs - {cs_p}, cc - {cc_p}')
# counter += 1
fig.show()

# %% Test out policies

test_out_policy(input_data, 10, mdp_policy, "MDP", betas)
# for cw_p in [1, 1.25, 1.5]:
#     for cs_p in [1, 1.25, 1.5]:
#         for cc_p in [1, 25, 50]:
            # print()
            # print()
            # print(f'COSTS: {cw_p}-cs {cs_p}-cc {cc_p}')
            
            # betas = read_betas(os.path.join(my_path, 'Data', f'Optimal-Betas-cw{cw_p}-cs{cs_p}-cc{cc_p}.xlsx'))
            # test_out_policy(input_data, 1, mdp_policy, 'MDP ', betas)
            # fig.add_subplot()

# %%