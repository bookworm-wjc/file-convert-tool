import json
def trans_ipnb_into_py(path):
    # read cells in the ipynb file into a list
    ipnb_f = open(path,'r',encoding='UTF-8')
    ipnb_f_data = ipnb_f.read()
    ipnb_f.close()
    data_dict = json.loads(ipnb_f_data)
    cell_list = data_dict['cells']

    # generate an object file
    file_name = path.split('/')[-1].split('.')[0]+'.py'
    py_f = open(f'./{file_name}','a',encoding='UTF-8')

    # write cells into the object file
    n = len(cell_list)
    for i in range(n):
        cell = cell_list[i]
        source = cell['source']
        # code cell
        if cell['cell_type']=='code':
            for j in range(len(source)):
                py_f.write(source[j])
            py_f.write('\n\n')
        # markdown cell, turn it into an annotation
        else:
            py_f.write('\nr"""\n')
            for j in range(len(source)):
                py_f.write(source[j])
            py_f.write('\n"""\n\n')

    py_f.close()


if __name__=='__main__':
    trans_ipnb_into_py('D:/Softwares/JupyterNotebookFiles/Machine Learning/Course2_Advanced_Learning_Algorithms/week3/work/C2_W3_Assignment.ipynb')
