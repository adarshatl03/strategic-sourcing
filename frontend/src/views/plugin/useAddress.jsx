import { useEffect, useState } from 'react';

const useGetCurrentAddress = () => {
    const [address, setAddress] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchAddress = async (latitude, longitude) => {
            try {
                const url = `https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}`;
                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error(`Error fetching address: ${response.statusText}`);
                }
                const data = await response.json();
                setAddress(data.address);
            } catch (err) {
                setError(err.message);
            }
        };

        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const { latitude, longitude } = position.coords;
                    fetchAddress(latitude, longitude);
                },
                (geoError) => {
                    setError(geoError.message);
                }
            );
        } else {
            setError("Geolocation is not supported by this browser.");
        }
    }, []);

    return { address, error };
};

export default useGetCurrentAddress;
