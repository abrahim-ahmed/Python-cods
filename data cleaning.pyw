    X = X.replace(to_replace='[!"#$%&\'()*+,/:;<=>?@[\\]^_`{|}~\.]',value=' ',regex=True) # remove punctuation except
    X = X.replace(to_replace='-',value=' ',regex=True) # remove -
    X = X.replace(to_replace='\s+',value=' ',regex=True) # remove new line
    X = X.replace(to_replace='  ',value='',regex=True) # remove double white space
