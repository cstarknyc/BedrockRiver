import numpy as np
import sympy as sy

from symbols import *
from utils import *

class empty_model():
    def __init__(self, params_dict=None):
        self.reset_params(params_dict=params_dict)
        self.figs={}
        self.pi = sy.pi
        
    def set_params(self, params_dict):
        for item in params_dict.items():
            setattr(self,str(item[0]),sy.N(item[1]))
    
    def reset_params(self, params_dict=None):
        self.default_params_dict = { 
            g: 9.81,
            Q: 1000.0,
            beta_0: 0.001,
            C: sy.sqrt(1e-3),
            n_m: 0.03,
            rho: 1000.0,
            rho_s: 2650.0,
            rho_Delta: 1650.0,
            rho_star_Delta: 1.650,
            D_fine:    2.0e-3,
            D_50:      4.0e-3,
            D_coarse: 20.0e-3,
            tau_star_c: 0.04,
            nu: 1e-3/1000.0, # 1.308e-3/1000.0 @ 10ºC, rho=1000
            E_star: E_star,
            F: F,
            phi:   phi,
            theta: theta,
            beta: beta,
            tau: tau,
            tau_star: tau_star,
            u_star: u_star,
            tau_star_fine: tau_star_fine,
            tau_star_coarse: tau_star_coarse,
            d: d,
            u: u,
            w: w,
            u_c: 0.0,
            u_i: 5.0,
            d_i: 50.0,
            q_b: q_b,
            q_bc: q_bc,
            q_star_bc: q_star_bc,
            q_s: q_s,
            q_c: q_c,
            q_w: q_w,
            epsilon_r: epsilon_r,
            mu: 0.75,
            Omega_r: Omega_r,
#             eta: 0.5,
            chi: chi,
            R: R,
            L: 1000.0,
            W: 50.0,
            U: 1.0
        }
        if params_dict is not None:
            self.default_params_dict.update(params_dict)
        for item in self.default_params_dict.items():
#             print(  str(item[0]),sy.N(item[1])  )
            setattr(self,str(item[0]),sy.N(item[1]))
#         print(self.default_params_dict)
         
    def get_params(self,var_precision_dict=None):
        if var_precision_dict is not None:
            result = {}
            for var_precision in var_precision_dict.items():
                vdi = {var_precision[0]:
                       getattr(self,str(var_precision[0])).round(var_precision[1])} \
                if var_precision[1] is not None else {str(var_precision[0]):
                                                      getattr(self,str(var_precision[0]))}
            result.update(vdi)
            return result
        else:
            params_list =  {
                'g',
                'Q',
                'beta_0', 
                'C', 
                'n_m', 
                'rho', 
                'rho_s', 
                'rho_Delta',
                'rho_star_Delta', 
                'D_fine',
                'D_coarse',
                'D_50',
                'tau_star_c',
                'nu',
                'u_c', 
                'mu', 
                'u_i', 
                'd_i',
#                 'eta',
                'L', 
                'W', 
                'U'
            }
        rtn_dict = {}
        for param in params_list:
#             print(var[0],type(var[0]))
            try:
                dict_update = {eval(param): getattr(self,str(eval(param)))}
            except:
                print(param, getattr(self,param))
                raise ValueError
            rtn_dict.update(dict_update)
        return rtn_dict
            

