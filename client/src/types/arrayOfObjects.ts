const arrayOfObject: Array<object> = JSON.parse(localStorage.getItem('urls') || '[]');

export default arrayOfObject;
