def distance_processing(processed_dictionary, researched_input, input_range):

    distance = [i for i in range(1,input_range+1)]
    snps_forward, snps_backward = [], []

    print(researched_input)
    current_snp = processed_dictionary.get(researched_input)
    print(current_snp)
    for snp in range(len(distance)):
        try:
            snps_forward.append(current_snp[0] + distance[snp])
            snps_backward.append(current_snp[0] - distance[snp])
        except:
            print("None type has been found. Check if your rsID really exists")
            break

    return snps_forward, snps_backward

def compare_values(processed_dictionary, researched_input, distance):

    current_snp = processed_dictionary.get(researched_input)
    
    with open('results.txt', 'w') as result_file:
        
        print(f"Current SNP: {current_snp[0]} | Position: {current_snp[1]} | Strandness: {current_snp[2]} \n\n", file = result_file)

        for key, value in processed_dictionary.items():
            for snp_value in range(len(distance[0])):
                if value[0] in distance[0] or value[0] in distance[1]:

                    print(f"SNP ID: rs{key} \nPosition: {value[0]} \nDistance: {value[0]-current_snp[0]} bp \nGenotype: {value[1]} \nStrandness: {value[2]} \n\n", file = result_file)
                    break           
                else:
                    continue