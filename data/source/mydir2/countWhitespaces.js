const countWhitespaces = (str) => {
    let count = 0;

    for (let i = 0; i < str.length; i++) {
        if (/\s/.test(str[i]))
            count++;
        return count;
    }
};

export { countWhitespaces };
