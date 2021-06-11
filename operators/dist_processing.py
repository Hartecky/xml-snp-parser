def distance_processing(processed_dictionary, researched_input, input_range):

    distance = [i for i in range(1,input_range+1)]
    snps_forward, snps_backward = [], []

    current_snp = processed_dictionary.get(researched_input)

    for snp in range(len(distance)):
        try:
            snps_forward.append(current_snp[0] + distance[snp])
            snps_backward.append(current_snp[0] - distance[snp])
        except:
            print("None type has been found. Check if your rsID really exists")
            break

    return snps_forward, snps_backward

def compare_values(processed_dictionary, researched_input, distance, gene_name):

    current_snp = processed_dictionary.get(researched_input)

    with open('results.txt', 'a+') as result_file:
        
        #print(f"Current SNP: {current_snp[0]} | Position: {current_snp[1]} | Strandness: {current_snp[2]} \n\n", file = result_file)
        for key, value in processed_dictionary.items():
            for snp_value in range(len(distance[0])):
                if value[0] in distance[0] or value[0] in distance[1]:

                    #print(f"SNP ID: {key} \nPosition: {value[0]} \nDistance: {value[0]-current_snp[0]} bp \nGenotype: {value[1]} \nStrandness: {value[2]} \n\n", file = result_file)

                    print(f"{gene_name};{researched_input};{current_snp[0]};{current_snp[1]};{current_snp[2]};{key};{value[0]};{value[0]-current_snp[0]};{value[1]};{value[2]}", file = result_file)
                    break           
                else:
                    continue

    print("Analysis completed")