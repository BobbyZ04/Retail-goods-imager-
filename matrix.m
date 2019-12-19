mat = zeros(5,5);
for i = 1:1:5 %loop through catagories
    for j = 1:1:10 %loop though all items in a specific catagory
    %   prediction = classify(image)
        prediction = classify();
        mat(i,prediction) = mat(i,prediction) + 1;
    end
end

function [prediction] = classify() % classify(image) use actual prediction function
    prediction = floor(rand * 5)+1;
end