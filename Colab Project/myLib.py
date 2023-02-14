def dataset_naming(title, version_1_or_2, test_size, data_processing, pca_reduction, num_of_principal_comp, frequency_range, time_window, time_bin_size, subject_list, experiment_list):
  title_app = str(title)
  lower_limit, upper_limit = frequency_range

  if version_1_or_2 : title_app += "_V1"
  else : title_app += "_V2"

  if pca_reduction : title_app += "_PCA" + str(num_of_principal_comp)

  if time_bin_size : title_app += "_TimeBin" + str(time_bin_size)

  if data_processing : title_app += "_" + data_processing.upper()

  title_app += "_Subject" + str(subject_list).replace(",", "-").replace(" ", "").replace("[", "").replace("]", "")
  title_app += "_Experiment" + str(experiment_list).replace(",", "-").replace(" ", "").replace("[", "").replace("]", "")

  title_app += "_Time_window-" + str(time_window[0]) + "-" + str(time_window[1])
  title_app += "_Freq-"+ str(lower_limit) + "-" + str(upper_limit)

  title_app += ".csv"

  return title_app

#dataset_naming("Dataset_training", version_1_or_2, test_size, data_processing, pca_reduction, #num_of_principal_comp, frequency_range, time_window, time_bin_size, subject_list, experiment_list)
