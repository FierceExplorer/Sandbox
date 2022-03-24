

layers = input("How many layers of the pyramid: ")

def pyramid(layers):
  layers = int(layers) 
  current_layer = 1
  while current_layer <= layers: 
    # Create Spaces 
    strspaces = ''
    nspaces = 1 
    while nspaces <= (layers - current_layer):
      strspaces = strspaces + ' '
      nspaces += 1 
    # Create Stars 
    strstars = ''
    nstars = 1 
    while nstars <= current_layer: 
      strstars = strstars + '* '
      nstars += 1 

    print(strspaces + strstars) 
    current_layer += 1 
  '''
  base = layers/2
  base = math.ceil(base)
  print(base)
  base_space = ''
  for q in range(base + 1): 
    base_space = base_space + ' '
  print(base_space + '***') '''
    

pyramid(layers)
