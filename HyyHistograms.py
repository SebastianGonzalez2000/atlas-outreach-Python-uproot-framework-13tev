myy = {
    # change plotting parameters                                                                                                     
    'bin_width':2,
    'num_bins':30,
    'xrange_min':100,
    'xlabel':r'$\mathrm{m_{\gamma\gamma}}$ [GeV]',
    'log_y':False,

    # change aesthetic parameters if you want                                                                                        
    'y_label_x_position':-0.09, # 0.09 to the left of y axis                                                                         
    'legend_loc':'lower left',
    'log_top_margin':10000, # to decrease the separation between data and the top of the figure, remove a 0                          
    'linear_top_margin':1.1 # to decrease the separation between data and the top of the figure, pick a number closer to 1           
}

hist_dict = {'myy':myy}
