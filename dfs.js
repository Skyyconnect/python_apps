let graph = {'A': new Set(['B', 'C']),
         'B': new Set(['A', 'D', 'E']),
         'C': new Set(['A', 'F']),
         'D': new Set(['B']),
         'E': new Set(['B', 'F']),
         'F': new Set(['C', 'E'])}


function findAllPathsFrom (graph, start , end){
  let node = {
    location: start,
    data: [start]
  },stack = [node],paths = [],path, vertex;

  while(stack){ 
    vertex = stack.shift();
    path = new Set(vertex.data);
    let difference = new Set([...graph[vertex.location]].filter(x => !path.has(x))), d = Array.from(difference);
    for( let key in d){
       node = {   
          location: d[key],
          data: Array.from(path)+[d[key]],  
        };
      console.log(node)
      if (node.location === end){
          paths.push(node);
          console.log(node)
      }else{
          stack.push(node);
      }
        
    }
        
  }
  return paths;
    
}
